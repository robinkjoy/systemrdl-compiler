import re
from parser.SystemRDLListener import SystemRDLListener
from parser.SystemRDLParser import SystemRDLParser
import Component


def extract_num(string):
    if string.isdigit():
        return int(string)
    elif string[0:2] in ('0x', '0X'):
        return int(string, 16)
    string = re.split('\'([bodh])', string, 1, flags=re.IGNORECASE)
    if string[2][0] == '_':
        exit('error: first position of value should not be \'_\'.')
    base = {'b': 2, 'd': 10, 'o': 8, 'h': 16}[string[1].lower()]
    return (int(string[0]), int(string[2].translate({ord('_'): None}), base))


class Listener(SystemRDLListener):

    COMPONENT_CLASS = {
        'addrmap': Component.AddrMap,
        'regfile': Component.RegFile,
        'reg': Component.Register,
        'field': Component.Field,
        'signal': Component.Signal
        }

    def __init__(self, parser):
        self.rule_names = parser.ruleNames
        self.curr_comp = None
        self.addrmaps = []
        self.definitions = [[]]
        self.user_def_props = []
        self.root_sig_insts = []
        self.defaults = [{}]

    def add_definition(self, definition):
        allowed_defs = {
            'Property': [],
            'Enum': [],
            'Signal': [],
            'Field': ['Signal', 'Enum'],
            'Register': ['Field', 'Signal', 'Enum'],
            'RegFile': ['Register', 'Field', 'Signal', 'Enum'],
            'AddrMap': ['RegFile', 'Register', 'Field', 'Signal', 'Enum']
            }
        comp_type = definition.get_type()
        if self.curr_comp is not None:
            curr_type = self.curr_comp.get_type()
            if comp_type not in allowed_defs[curr_type]:
                exit('error: {} definition not allowed in {}'.format(comp_type, curr_type))
        if any([x for x in self.definitions[-1] if x.def_id == definition.def_id]):
            exit('error: all definition names should be unique within a scope')
        self.definitions[-1].append(definition)

    def push_definitions(self):
        self.definitions.append([])

    def pop_definitions(self):
        self.definitions.pop()

    def get_definition(self, def_type, def_id):
        for defs in reversed(self.definitions):
            definition = [x for x in defs if isinstance(x, def_type) and x.def_id == def_id]
            if definition:
                return definition[0]
        return None

    def add_root_sig_inst(self, inst):
        if any([x for x in self.root_sig_insts if x.inst_id == inst.inst_id]):
            exit('error: all instance names should be unique within a scope')
        self.root_sig_insts.append(inst)

    def add_default(self, default):
        if default[0] in self.defaults[-1]:
            exit('error: defaults can be assigned only once per scope.')
        self.defaults[-1].update({default[0]: default[1]})

    def push_defaults(self):
        self.defaults.append({})

    def pop_defaults(self):
        self.defaults.pop()

    def get_default_value(self, prop):
        for defs in reversed(self.defaults):
            if prop in defs:
                return defs[prop]
        return None

    def get_post_inst_prop_value(self, ctx, prop):
        prop_token = {'reset': ('EQ', '='),
                      'at_addr': ('AT', '@'),
                      'inc_addr': ('INC', '+='),
                      'align_addr': ('MOD', '%=')}
        tok_method = getattr(ctx, prop_token[prop][0])
        if tok_method() is None:
            return None
        for i, tok in enumerate(ctx.children):
            if tok.getText() == prop_token[prop][1]:
                return extract_num(ctx.children[i+1].getText())

    def extract_rhs_value(self, ctx):
        if ctx.property_rvalue_constant() is not None:
            value_str = ctx.getText()
            childctx = ctx.getChild(0)
            if childctx.num() is not None:
                return extract_num(value_str)
            elif value_str == 'true':
                return True
            elif value_str == 'false':
                return False
            else:
                return value_str
        elif ctx.enum_body() is not None:
            return self.extract_enum_body(ctx.getChild(1), Component.Enum(None))
        elif ctx.instance_ref() is not None:
            return self.extract_instance_ref(ctx.getChild(0))
        elif ctx.concat() is not None:
            exit('error:{}: concat not implemented.',format(ctx.start.line))

    def extract_enum_body(self, ctx, enum):
        if len(ctx.enum_entry()) == 0:
            exit('error:{}: no entries in enum.'.format(ctx.start.line))
        for entryctx in ctx.children:
            if not isinstance(entryctx, SystemRDLParser.Enum_entryContext):
                continue
            name = entryctx.getChild(0).getText()
            value = extract_num(entryctx.getChild(2).getText())
            if not isinstance(value, tuple):
                exit('error:{}: enum entry value should be sizedNumeric'.format(entryctx.start.line))
            if any([x for x in enum.comps if x.def_id == name]):
                exit('error:{}: {} already defined in enum.'.format(entryctx.start.line, name))
            if len(enum.comps) != 0 and value[0] != enum.comps[0].value[0]:
                exit('error:{}: size does not match others.'.format(entryctx.start.line))
            if any([x for x in enum.comps if x.value == value]):
                exit('error:{}: {} already defined in enum.'.format(entryctx.start.line, entryctx.getChild(2).getText()))
            entry = Component.EnumEntry(name, value)
            for propctx in entryctx.children:
                if not isinstance(propctx, SystemRDLParser.Enum_property_assignContext):
                    continue
                setattr(entry, propctx.getChild(0).getText(), propctx.getChild(2).getText())
            enum.comps.append(entry)
        return enum

    def extract_instance_ref(self, ctx):
        prop = None
        for i, elemctx in enumerate(ctx.children):
            parent = self.curr_comp if i == 0 else inst
            if isinstance(elemctx, SystemRDLParser.Instance_ref_elemContext):
                def match(comp, inst_id):
                    if isinstance(comp, list):
                        return comp[0].inst_id == inst_id
                    else:
                        return comp.inst_id == inst_id
                if isinstance(parent, list):
                    exit('error:{}: array index for {} not specified.'.format(
                                            elemctx.start.line, parent.inst_id))
                inst_id = elemctx.getChild(0).getText()
                inst = next((x for x in parent.comps if match(x, inst_id)), None)
                if elemctx.num() is not None:
                    if not isinstance(inst, list):
                        exit('error:{}: {} is not an array'.format(
                            elemctx.start.line, inst.inst_id))
                    index = extract_num(elemctx.getChild(2).getText())
                    if isinstance(index, tuple):
                        exit('error:{}: array index should be numeric.'.format(
                                            elemctx.start.line))
                    inst = inst[index]
            elif isinstance(elemctx, SystemRDLParser.S_propertyContext):
                prop = elemctx.getChild(0).getText()
        return (inst, prop) if prop is not None else inst

    # Enter a parse tree produced by SystemRDLParser#root.
    def enterRoot(self, ctx:SystemRDLParser.RootContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#root.
    def exitRoot(self, ctx:SystemRDLParser.RootContext):
        # addrmaps defined but not instantiated
        self.addrmaps = [x for x in self.definitions[0] if isinstance(x, Component.AddrMap) and not x.instantiated]

    # Enter a parse tree produced by SystemRDLParser#property_definition.
    def enterProperty_definition(self, ctx:SystemRDLParser.Property_definitionContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_definition.
    def exitProperty_definition(self, ctx:SystemRDLParser.Property_definitionContext):
        pass



    # Enter a parse tree produced by SystemRDLParser#root.
    def enterRoot(self, ctx:SystemRDLParser.RootContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#root.
    def exitRoot(self, ctx:SystemRDLParser.RootContext):
        # addrmaps defined but not instantiated
        self.addrmaps = [x for x in self.definitions[0] if isinstance(x, Component.AddrMap) and not x.instantiated]

    # Enter a parse tree produced by SystemRDLParser#property_definition.
    def enterProperty_definition(self, ctx:SystemRDLParser.Property_definitionContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_definition.
    def exitProperty_definition(self, ctx:SystemRDLParser.Property_definitionContext):
        pass



    # Enter a parse tree produced by SystemRDLParser#root.
    def enterRoot(self, ctx:SystemRDLParser.RootContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#root.
    def exitRoot(self, ctx:SystemRDLParser.RootContext):
        # addrmaps defined but not instantiated
        self.addrmaps = [x for x in self.definitions[0] if isinstance(x, Component.AddrMap) and not x.instantiated]

    # Enter a parse tree produced by SystemRDLParser#property_definition.
    def enterProperty_definition(self, ctx:SystemRDLParser.Property_definitionContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_definition.
    def exitProperty_definition(self, ctx:SystemRDLParser.Property_definitionContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_body.
    def enterProperty_body(self, ctx:SystemRDLParser.Property_bodyContext):
        prop_id = ctx.parentCtx.getChild(0, SystemRDLParser.S_idContext).getText()
        if not ctx.property_type():
            exit('error:{}: property type not specified'.format(ctx.start.line))
        if len(ctx.property_type()) > 1:
            exit('error:{}: property type reassigned'.format(ctx.start.line))
        prop_type = ctx.getChild(0, SystemRDLParser.Property_typeContext).getChild(2).getText()
        if not ctx.property_usage():
            exit('error:{}: property usage not specified'.format(ctx.start.line))
        if len(ctx.property_usage()) > 1:
            exit('error:{}: property usage reassigned'.format(ctx.start.line))
        prop_usage = []
        prop_usage_ctx = ctx.getChild(0, SystemRDLParser.Property_usageContext)
        for childctx in prop_usage_ctx.getChildren():
            if isinstance(childctx, SystemRDLParser.Property_componentContext):
                prop_usage.append(childctx.getText())
        if len(ctx.property_default()) > 1:
            exit('error:{}: property default reassigned'.format(ctx.start.line))
        prop_default_ctx = ctx.getChild(0, SystemRDLParser.Property_defaultContext)
        prop_default_str = prop_default_ctx.getChild(2).getText()
        if prop_default_ctx.string() is not None:
            if prop_type != 'string':
                exit('error:{}: default does not match type.'.format(ctx.start.line))
            prop_default = prop_default_str
        elif prop_default_ctx.num() is not None:
            if prop_type != 'number':
                exit('error:{}: default does not match type.'.format(ctx.start.line))
            prop_default = extract_num(prop_default_str)
            if not isinstance(prop_default, int):
                exit('error:{}: default value cannot be sizedNumeric.'.format(ctx.start.line))
        else:
            if prop_type != 'boolean':
                exit('error:{}: default does not match type.'.format(ctx.start.line))
            prop_default = True if prop_default_str == 'true' else False
        self.user_def_props.append(Component.Property(prop_id, prop_type, prop_usage, prop_default))

    # Exit a parse tree produced by SystemRDLParser#property_body.
    def exitProperty_body(self, ctx:SystemRDLParser.Property_bodyContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_type.
    def enterProperty_type(self, ctx:SystemRDLParser.Property_typeContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_type.
    def exitProperty_type(self, ctx:SystemRDLParser.Property_typeContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_default.
    def enterProperty_default(self, ctx:SystemRDLParser.Property_defaultContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_default.
    def exitProperty_default(self, ctx:SystemRDLParser.Property_defaultContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_usage.
    def enterProperty_usage(self, ctx:SystemRDLParser.Property_usageContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_usage.
    def exitProperty_usage(self, ctx:SystemRDLParser.Property_usageContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_component.
    def enterProperty_component(self, ctx:SystemRDLParser.Property_componentContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_component.
    def exitProperty_component(self, ctx:SystemRDLParser.Property_componentContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_boolean_type.
    def enterProperty_boolean_type(self, ctx:SystemRDLParser.Property_boolean_typeContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_boolean_type.
    def exitProperty_boolean_type(self, ctx:SystemRDLParser.Property_boolean_typeContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_string_type.
    def enterProperty_string_type(self, ctx:SystemRDLParser.Property_string_typeContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_string_type.
    def exitProperty_string_type(self, ctx:SystemRDLParser.Property_string_typeContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_number_type.
    def enterProperty_number_type(self, ctx:SystemRDLParser.Property_number_typeContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_number_type.
    def exitProperty_number_type(self, ctx:SystemRDLParser.Property_number_typeContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_ref_type.
    def enterProperty_ref_type(self, ctx:SystemRDLParser.Property_ref_typeContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_ref_type.
    def exitProperty_ref_type(self, ctx:SystemRDLParser.Property_ref_typeContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#component_def.
    def enterComponent_def(self, ctx:SystemRDLParser.Component_defContext):
        comp_type = ctx.getChild(0).getText()
        # anonymous instatiation
        if ctx.getChild(1).getText() == '{':
            if self.curr_comp is None and comp_type != 'signal':            # (5.1.4)
                exit('error:{}: {} should not be instantiated in root scope.'.format(ctx.start.line, comp_type))
            comp = self.COMPONENT_CLASS[comp_type](None, None, self.curr_comp, self.defaults)
        # definition
        else:
            comp = self.COMPONENT_CLASS[comp_type](ctx.getChild(1).getText(), None, self.curr_comp, self.defaults)
            self.add_definition(comp)
        self.curr_comp = comp
        self.push_definitions()
        self.push_defaults()

    # Exit a parse tree produced by SystemRDLParser#component_def.
    def exitComponent_def(self, ctx:SystemRDLParser.Component_defContext):
        if ctx.getChild(1).getText() == '{' and ctx.anonymous_component_inst_elems() is None:
            exit('error:{}: definition name or instatiation name not specified.'.format(ctx.start.line))
        self.curr_comp = self.curr_comp.parent
        self.pop_definitions()
        self.pop_defaults()


    # Enter a parse tree produced by SystemRDLParser#explicit_component_inst.
    def enterExplicit_component_inst(self, ctx:SystemRDLParser.Explicit_component_instContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#explicit_component_inst.
    def exitExplicit_component_inst(self, ctx:SystemRDLParser.Explicit_component_instContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#anonymous_component_inst_elems.
    def enterAnonymous_component_inst_elems(self, ctx:SystemRDLParser.Anonymous_component_inst_elemsContext):
        if self.curr_comp.def_id is not None:
            exit('error:{}: both definition name and instantiation name specified.'.format(ctx.start.line))

    # Exit a parse tree produced by SystemRDLParser#anonymous_component_inst_elems.
    def exitAnonymous_component_inst_elems(self, ctx:SystemRDLParser.Anonymous_component_inst_elemsContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#component_inst_elem.
    def enterComponent_inst_elem(self, ctx:SystemRDLParser.Component_inst_elemContext):
        if self.rule_names[ctx.parentCtx.getRuleIndex()] == 'anonymous_component_inst_elems':
            comp = self.curr_comp
            parent = self.curr_comp.parent
        else:   # if explicit_component_inst
            comp_name = ctx.parentCtx.getChild(0, SystemRDLParser.S_idContext).getText()
            comp = self.get_definition(Component.Component, comp_name)
            if comp is None:
                exit('error:{}: component \'{}\' definition not found'.format(
                    ctx.parentCtx.start.line, comp_name))
            parent = self.curr_comp
        if ctx.array() is None:
            inst = comp.customcopy()
        else:
            # array indices
            if ctx.getChild(1).getChild(2).getText() == ':':
                inst = comp.customcopy()
                # (5.1.2.a.3.ii)
                if inst.get_type() != 'Field':    # Signal too??
                    exit('error:{}: array indices not allowed for {}'.format(
                        ctx.start.line, inst.get_type()))
                high = extract_num(ctx.getChild(1).getChild(1).getText())
                low = extract_num(ctx.getChild(1).getChild(3).getText())
                if not isinstance(high, int) or not isinstance(low, int):
                    exit('error:{}: array indices should be unsizedNumeric'.format(
                        ctx.start.line))
                inst.position = (high, low)
            else:
                size = extract_num(ctx.getChild(1).getChild(1).getText())
                if not isinstance(size, int):
                    exit('error:{}: array size should be unsizedNumeric'.format(
                        ctx.start.line))
                if comp.get_type() in ('Field', 'Signal'):
                    inst = comp.customcopy()
                    inst.size = size
                else:
                    inst = [comp.customcopy() for i in range(size)]
        inst_id = ctx.getChild(0).getText()
        if isinstance(inst, list):
            for x in inst:
                setattr(x, 'inst_id', inst_id)
                if x.name is None:
                    x.name = inst_id
                setattr(x, 'parent', parent)
        else:
            inst.inst_id = inst_id
            if inst.name is None:
                inst.name = inst_id
            inst.parent = parent
        for prop in ['reset', 'at_addr', 'inc_addr', 'align_addr']:
            value = self.get_post_inst_prop_value(ctx, prop)
            if value is not None:
                inst.set_property(prop, value, [], None) 
        # if in root, component is signal
        if parent is None:
            self.add_root_sig_inst(inst)
        else:
            parent.add_comp(inst)

    # Exit a parse tree produced by SystemRDLParser#component_inst_elem.
    def exitComponent_inst_elem(self, ctx:SystemRDLParser.Component_inst_elemContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#array.
    def enterArray(self, ctx:SystemRDLParser.ArrayContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#array.
    def exitArray(self, ctx:SystemRDLParser.ArrayContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#instance_ref.
    def enterInstance_ref(self, ctx:SystemRDLParser.Instance_refContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#instance_ref.
    def exitInstance_ref(self, ctx:SystemRDLParser.Instance_refContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#instance_ref_elem.
    def enterInstance_ref_elem(self, ctx:SystemRDLParser.Instance_ref_elemContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#instance_ref_elem.
    def exitInstance_ref_elem(self, ctx:SystemRDLParser.Instance_ref_elemContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_assign.
    def enterProperty_assign(self, ctx:SystemRDLParser.Property_assignContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_assign.
    def exitProperty_assign(self, ctx:SystemRDLParser.Property_assignContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#default_property_assign.
    def enterDefault_property_assign(self, ctx:SystemRDLParser.Default_property_assignContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#default_property_assign.
    def exitDefault_property_assign(self, ctx:SystemRDLParser.Default_property_assignContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#explicit_property_assign.
    def enterExplicit_property_assign(self, ctx:SystemRDLParser.Explicit_property_assignContext):
        if self.rule_names[ctx.parentCtx.getRuleIndex()] == 'default_property_assign':
            if ctx.property_modifier():
                exit('error:{}: property modifier not allowed in default'.format(ctx.start.line))
            prop = ctx.getChild(0).getText()
            if prop in ('name', 'desc'):
                if (ctx.property_assign_rhs() is None
                        or ctx.getChild(2).property_rvalue_constant() is None
                        or ctx.getChild(2).getChild(0).string() is None):
                    exit('error:{}: {} expected string value.'.format(ctx.start.line, prop))
                value = ctx.getChild(2).getText()
            else:
                def prop_class(prop):
                    for key, cls in self.COMPONENT_CLASS.items():
                        if prop in cls(None, None, [], []).properties:
                            return cls(None, None, [], [])
                    return None
                cls = prop_class(prop)
                if cls is None:
                    exit('error:{}: {} is not a builtin property.'.format(ctx.start.line, prop))
                if ctx.property_assign_rhs() is None:
                    value = True
                else:
                    value = self.extract_rhs_value(ctx.getChild(2))
                if not cls.check_type(prop, value):
                    exit('error:{}: {} expected {}.'.format(ctx.start.line, prop, cls.properties[prop]))
            self.add_default((prop, value))
        else:
            if ctx.property_modifier():
                if ctx.getChild(1).getText() != 'intr':
                    exit('error:{}: property modifier is allowed only for\'intr\''.format(ctx.start.line))
                self.curr_comp.set_property('intrmod', ctx.getChild(0).getText(), [], False) # fix nonsticky
                self.curr_comp.set_property('intr', True, [], False)
            else:
                prop = ctx.getChild(0).getText()
                if ctx.property_assign_rhs() is None:
                    value = True
                else:
                    value = self.extract_rhs_value(ctx.getChild(2))
                self.curr_comp.set_property(prop, value, self.user_def_props, False)

    # Exit a parse tree produced by SystemRDLParser#explicit_property_assign.
    def exitExplicit_property_assign(self, ctx:SystemRDLParser.Explicit_property_assignContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#post_property_assign.
    def enterPost_property_assign(self, ctx:SystemRDLParser.Post_property_assignContext):
        inst_prop = self.extract_instance_ref(ctx.getChild(0))
        if not isinstance(inst_prop, tuple):
            exit('error:{}: property is not specified.'.format(ctx.start.line))
        (inst, prop) = inst_prop
        if ctx.property_assign_rhs() is None:
            value = True
        else:
            value = self.extract_rhs_value(ctx.getChild(2))
        inst.set_property(prop, value, self.user_def_props, True)

    # Exit a parse tree produced by SystemRDLParser#post_property_assign.
    def exitPost_property_assign(self, ctx:SystemRDLParser.Post_property_assignContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_assign_rhs.
    def enterProperty_assign_rhs(self, ctx:SystemRDLParser.Property_assign_rhsContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_assign_rhs.
    def exitProperty_assign_rhs(self, ctx:SystemRDLParser.Property_assign_rhsContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#concat.
    def enterConcat(self, ctx:SystemRDLParser.ConcatContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#concat.
    def exitConcat(self, ctx:SystemRDLParser.ConcatContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#concat_elem.
    def enterConcat_elem(self, ctx:SystemRDLParser.Concat_elemContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#concat_elem.
    def exitConcat_elem(self, ctx:SystemRDLParser.Concat_elemContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#s_property.
    def enterS_property(self, ctx:SystemRDLParser.S_propertyContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#s_property.
    def exitS_property(self, ctx:SystemRDLParser.S_propertyContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_rvalue_constant.
    def enterProperty_rvalue_constant(self, ctx:SystemRDLParser.Property_rvalue_constantContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_rvalue_constant.
    def exitProperty_rvalue_constant(self, ctx:SystemRDLParser.Property_rvalue_constantContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_modifier.
    def enterProperty_modifier(self, ctx:SystemRDLParser.Property_modifierContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_modifier.
    def exitProperty_modifier(self, ctx:SystemRDLParser.Property_modifierContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#s_id.
    def enterS_id(self, ctx:SystemRDLParser.S_idContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#s_id.
    def exitS_id(self, ctx:SystemRDLParser.S_idContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#num.
    def enterNum(self, ctx:SystemRDLParser.NumContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#num.
    def exitNum(self, ctx:SystemRDLParser.NumContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#string.
    def enterString(self, ctx:SystemRDLParser.StringContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#string.
    def exitString(self, ctx:SystemRDLParser.StringContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#enum_def.
    def enterEnum_def(self, ctx:SystemRDLParser.Enum_defContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#enum_def.
    def exitEnum_def(self, ctx:SystemRDLParser.Enum_defContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#enum_body.
    def enterEnum_body(self, ctx:SystemRDLParser.Enum_bodyContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#enum_body.
    def exitEnum_body(self, ctx:SystemRDLParser.Enum_bodyContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#enum_entry.
    def enterEnum_entry(self, ctx:SystemRDLParser.Enum_entryContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#enum_entry.
    def exitEnum_entry(self, ctx:SystemRDLParser.Enum_entryContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#enum_property_assign.
    def enterEnum_property_assign(self, ctx:SystemRDLParser.Enum_property_assignContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#enum_property_assign.
    def exitEnum_property_assign(self, ctx:SystemRDLParser.Enum_property_assignContext):
        pass
