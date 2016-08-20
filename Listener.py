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
    base = {'b': 2, 'd': 10, 'o': 8, 'h': 16}[string[1][1].to_lower()]
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
        self.userdefprops = []
        self.root_sig_insts = []

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

    def add_root_sig_inst(self, inst):
        if any([x for x in self.root_sig_insts if x.inst_id == inst.inst_id]):
            exit('error: all instance names should be unique within a scope')
        self.root_sig_insts.append(inst)

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
        pass

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
            comp = self.COMPONENT_CLASS[comp_type](None, None, self.curr_comp)
        # definition
        else:
            comp = self.COMPONENT_CLASS[comp_type](ctx.getChild(1).getText(), None, self.curr_comp)
            self.add_definition(comp)
        self.curr_comp = comp
        self.push_definitions()

    # Exit a parse tree produced by SystemRDLParser#component_def.
    def exitComponent_def(self, ctx:SystemRDLParser.Component_defContext):
        if ctx.getChild(1).getText() == '{' and ctx.anonymous_component_inst_elems() is None:
            exit('error:{}: definition name or instatiation name not specified.'.format(ctx.start.line))
        self.curr_comp = self.curr_comp.parent
        self.pop_definitions()


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
        #print(dir(ctx.getToken(SystemRDLParser.EQ, 0)))
        for child in ctx.children:
            if child.getText() == '=':
                print(child.getText())
        if isinstance(inst, list):
            for x in inst:
                setattr(x, 'inst_id', inst_id)
                setattr(x, 'parent', parent)
        else:
            inst.inst_id = inst_id
            inst.parent = parent
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
        pass

    # Exit a parse tree produced by SystemRDLParser#explicit_property_assign.
    def exitExplicit_property_assign(self, ctx:SystemRDLParser.Explicit_property_assignContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#post_property_assign.
    def enterPost_property_assign(self, ctx:SystemRDLParser.Post_property_assignContext):
        pass

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
