import re
from parser.SystemRDLListener import SystemRDLListener
from parser.SystemRDLParser import SystemRDLParser
import Component


def error(line, msg, *args):
    exit('error:{}: '.format(line) + msg.format(*args))


def extract_num(string, line):
    if string.isdigit():
        return int(string)
    elif string[0:2] in ('0x', '0X'):
        return int(string, 16)
    string = re.split('\'([bodh])', string, 1, flags=re.IGNORECASE)
    if string[2][0] == '_':
        error(line, 'first position of value should not be \'_\'.')
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
        self.assigned_props = [[]]

    def add_definition(self, definition, line):
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
                error(line, '{} definition not allowed in {}',
                      comp_type, curr_type)
        if any([x for x in self.definitions[-1] if x.def_id == definition.def_id]):
            error(line, 'all definition names should be unique within a scope')
        self.definitions[-1].append(definition)

    def push_scope(self):
        self.definitions.append([])
        self.defaults.append({})
        self.assigned_props.append([])

    def pop_scope(self):
        self.definitions.pop()
        self.defaults.pop()
        self.assigned_props.pop()

    def get_definition(self, def_type, def_id):
        for defs in reversed(self.definitions):
            definition = [x for x in defs
                          if isinstance(x, def_type) and x.def_id == def_id]
            if definition:
                return definition[0]
        return None

    def add_root_sig_inst(self, inst, line):
        if any([x for x in self.root_sig_insts if x.inst_id == inst.inst_id]):
            error(line, 'all instance names should be unique within a scope')
        self.root_sig_insts.append(inst)

    def add_default(self, default, line):
        if default[0] in self.defaults[-1]:
            error(line, 'defaults can be assigned only once per scope.')
        self.defaults[-1].update({default[0]: default[1]})

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
                num_str = ctx.children[i + 1].getText()
                line = ctx.children[i + 1].start.line
                return extract_num(num_str, line)

    def extract_rhs_value(self, ctx, prop):
        if ctx.property_rvalue_constant() is not None:
            value_str = ctx.getText()
            childctx = ctx.getChild(0)
            if childctx.num() is not None:
                return extract_num(value_str, childctx.start.line)
            elif value_str == 'true':
                return True
            elif value_str == 'false':
                return False
            else:
                return value_str
        elif ctx.enum_body() is not None:
            return self.extract_enum_body(ctx.getChild(1), Component.Enum(None))
        elif ctx.instance_ref() is not None:
            if prop == 'encode':
                # encode value is enum definition. not instances
                return self.get_definition(Component.Enum, ctx.getText())
            else:
                return self.extract_instance_ref(ctx.getChild(0))
        elif ctx.concat() is not None:
            error(ctx.start.line, 'concat not implemented.')

    def extract_enum_body(self, ctx, enum):
        if len(ctx.enum_entry()) == 0:
            error(ctx.start.line, 'no entries in enum.')
        for entryctx in ctx.children:
            if not isinstance(entryctx, SystemRDLParser.Enum_entryContext):
                continue
            name = entryctx.getChild(0).getText()
            value = extract_num(entryctx.getChild(2).getText(),
                                entryctx.getChild(2).start.line)
            if not isinstance(value, tuple):
                error(entryctx.start.line,
                      'enum entry value should be sizedNumeric')
            if any([x for x in enum.comps if x.def_id == name]):
                error(entryctx.start.line, '{} already defined in enum.', name)
            if len(enum.comps) != 0 and value[0] != enum.comps[0].value[0]:
                error(entryctx.start.line, 'size does not match others.')
            if any([x for x in enum.comps if x.value == value]):
                error(entryctx.start.line, '{} already defined in enum.',
                      entryctx.getChild(2).getText())
            entry = Component.EnumEntry(name, value)
            for propctx in entryctx.children:
                if not isinstance(propctx, SystemRDLParser.Enum_property_assignContext):
                    continue
                setattr(entry, propctx.getChild(0).getText(),
                        propctx.getChild(2).getText())
            enum.comps.append(entry)
        return enum

    def extract_instance_ref(self, ctx):
        prop = None
        inst = None
        for i, elemctx in enumerate(ctx.children):
            parent = self.curr_comp if i == 0 else inst
            if isinstance(elemctx, SystemRDLParser.Instance_ref_elemContext):
                line = elemctx.start.line
                def match(comp, inst_id):
                    if isinstance(comp, list):
                        return comp[0].inst_id == inst_id
                    else:
                        return comp.inst_id == inst_id
                if isinstance(parent, list):
                    error(line, 'array index for {} not specified.',
                          parent[0].inst_id)
                inst_id = elemctx.getChild(0).getText()
                inst = next((x for x in parent.comps
                             if match(x, inst_id)), None)
                if inst is None:
                    error(elemctx.start.line, '{} not found', inst_id)
                if elemctx.num() is not None:
                    if not isinstance(inst, list):
                        error(line, '{} is not an array', inst.inst_id)
                    index = extract_num(elemctx.getChild(2).getText(),
                                        elemctx.getChild(2).start.line)
                    if isinstance(index, tuple):
                        error(line, 'array index should be numeric.')
                    if index >= len(inst):
                        error(elemctx.start.line, 'array index out of range')
                    inst = inst[index]
            elif isinstance(elemctx, SystemRDLParser.S_propertyContext):
                prop = elemctx.getChild(0).getText()
        return (inst, prop) if prop is not None else inst

    def get_implicit_value(self, inst, prop, ctx):
        if ctx.s_id() is None:      # not user defined property
            return True
        else:
            return None

    def check_property_already_set(self, inst, prop, line):
        # (5.1.3.1) ex in (5.1.4)
        if (id(inst), prop) in self.assigned_props[-1]:
            error(line, 'property \'{}\' already assigned in scope', prop)
        self.assigned_props[-1].append((id(inst), prop))

    # Exit a parse tree produced by SystemRDLParser#root.
    def exitRoot(self, ctx):
        # addrmaps defined but not instantiated
        self.addrmaps = [x for x in self.definitions[0]
                         if isinstance(x, Component.AddrMap)
                         and not x.instantiated]
        for addrmap in self.addrmaps:
            addrmap.post_validate()

    # Enter a parse tree produced by SystemRDLParser#property_body.
    def enterProperty_body(self, ctx):
        prop_id = ctx.parentCtx.getChild(
            0, SystemRDLParser.S_idContext).getText()
        if not ctx.property_type():
            error(ctx.start.line, 'property type not specified')
        if len(ctx.property_type()) > 1:
            error(ctx.start.line, 'property type reassigned')
        prop_type = ctx.getChild(
            0, SystemRDLParser.Property_typeContext).getChild(2).getText()
        if not ctx.property_usage():
            error(ctx.start.line, 'property usage not specified')
        if len(ctx.property_usage()) > 1:
            error(ctx.start.line, 'property usage reassigned')
        prop_usage = []
        prop_usage_ctx = ctx.getChild(0, SystemRDLParser.Property_usageContext)
        for childctx in prop_usage_ctx.getChildren():
            if isinstance(childctx, SystemRDLParser.Property_componentContext):
                prop_usage.append(childctx.getText())
        if len(ctx.property_default()) > 1:
            error(ctx.start.line, 'property default reassigned')
        if not ctx.property_default():
            prop_default = None
        else:
            prop_default_ctx = ctx.getChild(
                0, SystemRDLParser.Property_defaultContext)
            prop_default_str = prop_default_ctx.getChild(2).getText()
            line = prop_default_ctx.start.line
            if prop_default_ctx.string() is not None:
                if prop_type != 'string':
                    error(line, 'default does not match type.')
                prop_default = prop_default_str
            elif prop_default_ctx.num() is not None:
                if prop_type != 'number':
                    error(line, 'default does not match type.')
                prop_default = extract_num(
                    prop_default_str, prop_default_ctx.start.line)
                if not isinstance(prop_default, int):
                    error(line, 'default value cannot be sizedNumeric.')
            else:
                if prop_type != 'boolean':
                    error(line, 'default does not match type.')
                prop_default = True if prop_default_str == 'true' else False
        self.user_def_props.append(
            Component.Property(prop_id, prop_type, prop_usage, prop_default))

    # Enter a parse tree produced by SystemRDLParser#component_def.
    def enterComponent_def(self, ctx):
        comp_type = ctx.getChild(0).getText()
        # anonymous instatiation
        if ctx.getChild(1).getText() == '{':
            # (5.1.4)
            if self.curr_comp is None and comp_type != 'signal':
                error(ctx.start.line,
                      '{} should not be instantiated in root scope.', comp_type)
            comp = self.COMPONENT_CLASS[comp_type](
                None, None, self.curr_comp, self.defaults, ctx.start.line)
        # definition
        else:
            comp = self.COMPONENT_CLASS[comp_type](ctx.getChild(1).getText(),
                                                   None, self.curr_comp,
                                                   self.defaults, ctx.start.line)
            self.add_definition(comp, ctx.start.line)
        self.curr_comp = comp
        self.push_scope()

    # Exit a parse tree produced by SystemRDLParser#component_def.
    def exitComponent_def(self, ctx):
        if (ctx.getChild(1).getText() == '{'
                and ctx.anonymous_component_inst_elems() is None):
            error(ctx.start.line,
                  'definition name or instatiation name not specified.')
        comp_child = {
            'Register': ['Field'],
            'RegFile': ['Register'],
            'AddrMap': ['AddrMap', 'RegFile', 'Register']
        }
        comp_type = self.curr_comp.get_type()
        def match(comp, ctype):
            if isinstance(comp, list):
                return comp[0].get_type() in comp_child[ctype]
            else:
                return comp.get_type() in comp_child[ctype]
        if comp_type in comp_child:
            if not any([x for x in self.curr_comp.comps if match(x, comp_type)]):
                error(ctx.start.line, 'no child components in {}', comp_type)
        if ctx.anonymous_component_inst_elems() is None and comp_type == 'Register':
            self.curr_comp.validate_fields()
        self.curr_comp = self.curr_comp.parent
        self.pop_scope()

    # Enter a parse tree produced by
    # SystemRDLParser#anonymous_component_inst_elems.
    def enterAnonymous_component_inst_elems(self, ctx):
        if self.curr_comp.def_id is not None:
            error(ctx.start.line,
                  'both definition name and instantiation name specified.')

    # Enter a parse tree produced by SystemRDLParser#component_inst_elem.
    def enterComponent_inst_elem(self, ctx):
        if self.rule_names[ctx.parentCtx.getRuleIndex()] == 'anonymous_component_inst_elems':
            comp = self.curr_comp
            parent = self.curr_comp.parent
        else:   # if explicit_component_inst
            comp_name = ctx.parentCtx.getChild(
                0, SystemRDLParser.S_idContext).getText()
            comp = self.get_definition(Component.Component, comp_name)
            if comp is None:
                error(ctx.parentCtx.start.line,
                      'component \'{}\' definition not found', comp_name)
            parent = self.curr_comp
        comp_type = comp.get_type()
        if ctx.array() is None:
            inst = comp.customcopy()
        else:
            indctx = ctx.getChild(1).getChild
            # array indices
            if ctx.getChild(1).getChild(2).getText() == ':':
                inst = comp.customcopy()
                # (5.1.2.a.3.ii)
                if comp_type != 'Field':    # Signal too??
                    error(ctx.start.line, 'array indices not allowed for {}', comp_type)
                high = extract_num(indctx(1).getText(), indctx(1).start.line)
                low = extract_num(indctx(3).getText(), indctx(3).start.line)
                if not isinstance(high, int) or not isinstance(low, int):
                    error(ctx.start.line, 'array indices should be unsizedNumeric')
                inst.position = (high, low)
                size = high - low + 1
            else:
                size = extract_num(indctx(1).getText(), indctx(1).start.line)
                if not isinstance(size, int):
                    error(ctx.start.line, 'array size should be unsizedNumeric')
                if comp_type in ('Field', 'Signal'):
                    inst = comp.customcopy()
                else:
                    inst = [comp.customcopy() for i in range(size)]
            if comp_type in ('Field', 'Signal'):
                width = {'Field': 'fieldwidth',
                         'Signal': 'signalwidth'}[comp_type]
                inst.set_property(width, size, ctx.start.line, [], False)
        inst_id = ctx.getChild(0).getText()
        if isinstance(inst, list):
            for i in inst:
                i.inst_id = inst_id
                i.parent = parent
                if i.name is None:
                    i.name = inst_id
                i.line = ctx.start.line
        else:
            inst.inst_id = inst_id
            inst.parent = parent
            if inst.name is None:
                inst.name = inst_id
            inst.line = ctx.start.line
        for prop in ['reset', 'at_addr', 'inc_addr', 'align_addr']:
            value = self.get_post_inst_prop_value(ctx, prop)
            if value is not None:
                if isinstance(inst, list):
                    for x in inst:
                        x.set_property(prop, value, ctx.start.line, [], None)
                else:
                    inst.set_property(prop, value, ctx.start.line, [], None)
        # if in root, component is signal
        if parent is None:
            self.add_root_sig_inst(inst, ctx.start.line)
        else:
            parent.add_comp(inst, ctx.start.line)

    # Enter a parse tree produced by SystemRDLParser#explicit_property_assign.
    def enterExplicit_property_assign(self, ctx):
        if self.rule_names[ctx.parentCtx.getRuleIndex()] == 'default_property_assign':
            if ctx.property_modifier():
                error(ctx.start.line, 'property modifier not allowed in default')
            prop = ctx.getChild(0).getText()
            if prop in ('name', 'desc'):
                if (ctx.property_assign_rhs() is None
                        or ctx.getChild(2).property_rvalue_constant() is None
                        or ctx.getChild(2).getChild(0).string() is None):
                    error(ctx.start.line, '{} expected string value.', prop)
                value = ctx.getChild(2).getText()
            else:
                def prop_class(prop):
                    for key, cls in self.COMPONENT_CLASS.items():
                        if prop in cls(None, None, [], [], None).properties:
                            return cls(None, None, [], [], None)
                    return None
                cls = prop_class(prop)
                if cls is None:
                    error(ctx.start.line, '{} is not a builtin property.', prop)
                if ctx.property_assign_rhs() is None:
                    value = True
                else:
                    value = self.extract_rhs_value(ctx.getChild(2), prop)
                if not cls.check_type(prop, value, ctx.start.line):
                    error(ctx.start.line, '{} expected {}.', prop, cls.properties[prop])
            self.add_default((prop, value), ctx.start.line)
        else:
            comp = self.curr_comp
            if ctx.property_modifier():
                if ctx.getChild(1).getText() != 'intr' or comp.get_type() != 'Field':
                    error(ctx.start.line, 'property modifier is allowed only for\'intr\' on Field')
                self.check_property_already_set(comp, 'intr', ctx.start.line)
                comp.set_property('intrmod', ctx.getChild(0).getText(),
                                  ctx.start.line, [], False)            # fix nonsticky
                comp.set_property('intr', True, ctx.start.line, [], False)
            else:
                prop = ctx.getChild(0).getText()
                if ctx.property_assign_rhs() is None:
                    value = self.get_implicit_value(
                        comp, prop, ctx.getChild(0))
                else:
                    value = self.extract_rhs_value(ctx.getChild(2), prop)
                self.check_property_already_set(comp, prop, ctx.start.line)
                comp.set_property(
                    prop, value, ctx.start.line, self.user_def_props, False)

    # Enter a parse tree produced by SystemRDLParser#post_property_assign.
    def enterPost_property_assign(self, ctx):
        inst_prop = self.extract_instance_ref(ctx.getChild(0))
        if not isinstance(inst_prop, tuple):
            error(ctx.start.line, 'property is not specified.')
        (inst, prop) = inst_prop
        if ctx.property_assign_rhs() is None:
            value = self.get_implicit_value(
                inst, prop, ctx.getChild(0).getChild(0, SystemRDLParser.S_propertyContext))
        else:
            value = self.extract_rhs_value(ctx.getChild(2), prop)
        self.check_property_already_set(inst, prop, ctx.start.line)
        if isinstance(inst, list):
            [x.set_property(prop, value, ctx.start.line, self.user_def_props, True) for x in inst]
        else:
            inst.set_property(prop, value, ctx.start.line, self.user_def_props, True)

    # Enter a parse tree produced by SystemRDLParser#enum_def.
    def enterEnum_def(self, ctx):
        enum = Component.Enum(ctx.getChild(1).getText())
        self.extract_enum_body(ctx.getChild(2), enum)
        self.add_definition(enum, ctx.start.line)
