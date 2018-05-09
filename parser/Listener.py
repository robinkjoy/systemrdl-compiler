import logging
import re

import Component
from Common import itercomps0
from parser.antlr.SystemRDLListener import SystemRDLListener
from parser.antlr.SystemRDLParser import SystemRDLParser

log = logging.getLogger()


def extract_num(string, line):
    if string.isdigit():
        return int(string)
    elif string[0:2] in ('0x', '0X'):
        return int(string, 16)
    # sized Number
    string = re.split('\'([bodh])', string, 1, flags=re.IGNORECASE)
    if string[2][0] == '_':
        log.error('first position of value should not be \'_\'.', line)
    base = {'b': 2, 'd': 10, 'o': 8, 'h': 16}[string[1].lower()]
    size = int(string[0])
    number = int(string[2].translate({ord('_'): None}), base)
    if number >= 2 ** size:
        log.error('Number does not fit within specified bit width', line)
    return size, number


def itercomp(comp):
    if isinstance(comp, list):
        for c in comp:
            yield c
    else:
        yield comp


def is_matching_instance(comp, inst_id):
    if isinstance(comp, list):
        return comp[0].inst_id == inst_id
    else:
        return comp.inst_id == inst_id


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
        self.signals = []
        self.scoped_insts = [[]]
        self.defaults = [{}]
        self.assigned_props = [[]]
        self.internal_signals = []

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
                log.error(f'{comp_type} definition not allowed in {curr_type}', line)
        if any([x for x in self.definitions[-1] if x.def_id == definition.def_id]):
            log.error('all definition names should be unique within a scope', line)
        self.definitions[-1].append(definition)

    def push_scope(self):
        self.definitions.append([])
        self.defaults.append({})
        self.assigned_props.append([])
        self.scoped_insts.append([])

    def pop_scope(self):
        self.definitions.pop()
        self.defaults.pop()
        self.assigned_props.pop()
        self.scoped_insts.pop()

    def get_definition(self, def_type, def_id):
        for defs in reversed(self.definitions):
            definition = next((x for x in defs
                               if isinstance(x, def_type) and x.def_id == def_id), None)
            if definition:
                return definition
        return None

    def add_root_sig_inst(self, inst, line):
        if any([x for x in self.signals if x.inst_id == inst.inst_id]):
            log.error('all instance names should be unique within a scope', line)
        self.signals.append(inst)

    def add_default(self, default, line):
        if default[0] in self.defaults[-1]:
            log.error('defaults can be assigned only once per scope.', line)
        self.defaults[-1].update({default[0]: default[1]})

    @staticmethod
    def get_post_inst_prop_value(ctx, prop):
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

    def extract_rhs_value(self, ctx, lprop):
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
            if lprop == 'encode':
                # encode value is enum definition. not instances
                return self.get_definition(Component.Enum, ctx.getText())
            else:
                inst, prop = self.extract_instance_ref_rhs(ctx.getChild(0))
                # fixme add checks on inst and prop
                if inst.get_type() == 'Signal':
                    if lprop in Component.Field.OUTPUT_SIG_PROPS:
                        if inst.output:
                            log.error(f'signal {inst.inst_id} already driven', ctx.start.line)
                        inst.output = True
                    else:
                        inst.input = True
                    return inst
                elif prop is not None:
                    sig_inst = Component.Signal(None, inst.inst_id + '_' + prop, None, [], ctx.start.line)
                    sig_inst.int_ref = (inst, prop)
                    log.debug(f'{sig_inst} {sig_inst.int_ref}')
                    setattr(sig_inst, 'signalwidth', 1)
                    self.internal_signals.append(sig_inst)
                    return sig_inst
                elif inst.get_type() == 'Field':
                    sig_inst = Component.Signal(None, inst.inst_id, None, [], ctx.start.line)
                    sig_inst.int_ref = (inst, None)
                    setattr(sig_inst, 'signalwidth', inst.fieldwidth)
                    self.internal_signals.append(sig_inst)
                    return sig_inst
        elif ctx.concat() is not None:
            log.error('concat not implemented.', ctx.start.line)

    @staticmethod
    def extract_enum_body(ctx, enum):
        if len(ctx.enum_entry()) == 0:
            log.error('no entries in enum.', ctx.start.line)
        for entryctx in ctx.children:
            if not isinstance(entryctx, SystemRDLParser.Enum_entryContext):
                continue
            name = entryctx.getChild(0).getText()
            value = extract_num(entryctx.getChild(2).getText(),
                                entryctx.getChild(2).start.line)
            if not isinstance(value, tuple):
                log.error('enum entry value should be sizedNumeric', entryctx.start.line)
            if any([x for x in enum.comps if x.def_id == name]):
                log.error(f'{name} already defined in enum.', entryctx.start.line)
            if len(enum.comps) != 0 and value[0] != enum.comps[0].value[0]:
                log.error('size does not match others.', entryctx.start.line)
            if any([x for x in enum.comps if x.value == value]):
                log.error(f'{entryctx.getChild(2).getText()} already defined in enum.', entryctx.start.line)
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
        parent = self.curr_comp
        for elemctx in ctx.children:
            if isinstance(elemctx, SystemRDLParser.Instance_ref_elemContext):
                line = elemctx.start.line
                # if array index not specified, applies to all. But array index should be
                # specified to access a child component
                if isinstance(parent, list):
                    log.error(f'array index for {parent[0].inst_id} not specified.', line)
                inst_id = elemctx.getChild(0).getText()
                inst = next((x for x in parent.comps + parent.signals
                             if is_matching_instance(x, inst_id)), None)
                if inst is None:
                    log.error(f'{inst_id} not found', elemctx.start.line)
                if elemctx.num() is not None:
                    if not isinstance(inst, list):
                        log.error('{inst.inst_id} is not an array', line)
                    index = extract_num(elemctx.getChild(2).getText(),
                                        elemctx.getChild(2).start.line)
                    if isinstance(index, tuple):
                        log.error('array index should be numeric.', line)
                    if index >= len(inst):
                        log.error('array index out of range', elemctx.start.line)
                    inst = inst[index]
            elif isinstance(elemctx, SystemRDLParser.S_propertyContext):
                prop = elemctx.getChild(0).getText()
            parent = inst
        return inst, prop

    def extract_instance_ref_rhs(self, ctx):
        prop = None
        inst = None
        parent = None
        line = ctx.start.line
        for elemctx in ctx.children:
            if parent is None:
                inst_id = elemctx.getChild(0).getText()
                for insts in reversed(self.scoped_insts):
                    inst = next((x for x in insts
                                 if is_matching_instance(x, inst_id)), None)
                    if inst:
                        break
                if inst is None:
                    log.error(f'{inst_id} not found', line)
            elif isinstance(elemctx, SystemRDLParser.Instance_ref_elemContext):
                inst_id = elemctx.getChild(0).getText()
                inst = next((x for x in parent.comps + parent.signals
                             if is_matching_instance(x, inst_id)), None)
                if inst is None:
                    log.error(f'{inst_id} not found', line)
                if elemctx.num() is not None:
                    if not isinstance(inst, list):
                        log.error('{inst.inst_id} is not an array', line)
                    index = extract_num(elemctx.getChild(2).getText(),
                                        elemctx.getChild(2).start.line)
                    if isinstance(index, tuple):
                        log.error('array index should be numeric.', line)
                    if index >= len(inst):
                        log.error('array index out of range', line)
                    inst = inst[index]
            elif isinstance(elemctx, SystemRDLParser.S_propertyContext):
                prop = elemctx.getChild(0).getText()
            if isinstance(inst, list):
                log.error(f'array index for {inst[0].inst_id} not specified.', line)
            parent = inst
        return inst, prop

    @staticmethod
    def get_implicit_value(ctx):
        if ctx.s_id() is None:  # not user defined property
            return True
        else:
            return None

    def check_property_already_set(self, inst, prop, line):
        # (5.1.3.1) ex in (5.1.4)
        if (id(inst), prop) in self.assigned_props[-1]:
            log.error(f'property \'{prop}\' already assigned in scope', line)
        self.assigned_props[-1].append((id(inst), prop))

    # Exit a parse tree produced by SystemRDLParser#root.
    def exitRoot(self, ctx):
        # addrmaps which are defined but not instantiated
        self.addrmaps = [x for x in self.definitions[0]
                         if isinstance(x, Component.AddrMap)
                         and not x.instantiated]
        if not self.addrmaps:
            log.error('No addressmaps found')

    # Enter a parse tree produced by SystemRDLParser#property_body.
    def enterProperty_body(self, ctx):
        prop_id = ctx.parentCtx.getChild(
            0, SystemRDLParser.S_idContext).getText()
        if not ctx.property_type():
            log.error('property type not specified', ctx.start.line)
        if len(ctx.property_type()) > 1:
            log.error('property type reassigned', ctx.start.line)
        prop_type = ctx.getChild(
            0, SystemRDLParser.Property_typeContext).getChild(2).getText()
        if not ctx.property_usage():
            log.error('property usage not specified', ctx.start.line)
        if len(ctx.property_usage()) > 1:
            log.error('property usage reassigned', ctx.start.line)
        prop_usage = []
        prop_usage_ctx = ctx.getChild(0, SystemRDLParser.Property_usageContext)
        for childctx in prop_usage_ctx.getChildren():
            if isinstance(childctx, SystemRDLParser.Property_componentContext):
                prop_usage.append(childctx.getText())
        if len(ctx.property_default()) > 1:
            log.error('property default reassigned', ctx.start.line)
        if not ctx.property_default():
            prop_default = None
        else:
            prop_default_ctx = ctx.getChild(
                0, SystemRDLParser.Property_defaultContext)
            prop_default_str = prop_default_ctx.getChild(2).getText()
            line = prop_default_ctx.start.line
            if prop_default_ctx.string() is not None:
                if prop_type != 'string':
                    log.error('default does not match type.', line)
                prop_default = prop_default_str
            elif prop_default_ctx.num() is not None:
                if prop_type != 'number':
                    log.error('default does not match type.', line)
                prop_default = extract_num(
                    prop_default_str, prop_default_ctx.start.line)
                if not isinstance(prop_default, int):
                    log.error('default value cannot be sizedNumeric.', line)
            else:
                if prop_type != 'boolean':
                    log.error('default does not match type.', line)
                prop_default = True if prop_default_str == 'true' else False
        self.user_def_props.append(
            Component.Property(prop_id, prop_type, prop_usage, prop_default))

    # Enter a parse tree produced by SystemRDLParser#component_def.
    # enter definitions and anonymous instatiations
    def enterComponent_def(self, ctx):
        comp_type = ctx.getChild(0).getText()
        # anonymous instatiation
        if ctx.getChild(1).getText() == '{':
            # (5.1.4)
            if self.curr_comp is None and comp_type != 'signal':
                log.error('{comp_type} should not be instantiated in root scope.', ctx.start.line)
            comp = self.COMPONENT_CLASS[comp_type](
                None, None, self.curr_comp, self.defaults, ctx.start.line)
        # definition
        else:
            comp = self.COMPONENT_CLASS[comp_type](ctx.getChild(1).getText(),
                                                   None, self.curr_comp,
                                                   self.defaults, ctx.start.line)
            self.add_definition(comp, ctx.start.line)
        # set bit order
        if (comp_type in ['addrmap', 'regfile', 'reg'] and
                self.curr_comp is not None and
                self.curr_comp.bit_order is not None):
            comp.bit_order = self.curr_comp.bit_order
        self.curr_comp = comp
        self.push_scope()

    # Exit a parse tree produced by SystemRDLParser#component_def.
    # exit definitions and anonymous instatiations
    def exitComponent_def(self, ctx):
        if (ctx.getChild(1).getText() == '{'
                and ctx.anonymous_component_inst_elems() is None):
            log.error('definition name or instatiation name not specified.', ctx.start.line)
        # at least one child component instantiated
        comp_child = {
            'Register': ['Field'],
            'RegFile': ['Register'],
            'AddrMap': ['AddrMap', 'RegFile', 'Register']
        }
        comp = self.curr_comp
        comp_type = comp.get_type()
        if comp_type in comp_child:
            if not any([x for x in itercomps0(comp.comps)
                        if x.get_type() in comp_child[comp_type]]):
                log.error('no child components in {comp_type}', ctx.start.line)
        # exit scope
        self.curr_comp = comp.parent
        self.pop_scope()

    # Enter a parse tree produced by
    # SystemRDLParser#anonymous_component_inst_elems.
    def enterAnonymous_component_inst_elems(self, ctx):
        if self.curr_comp.def_id is not None:
            log.error('both definition name and instantiation name specified.', ctx.start.line)

    # Exit a parse tree produced by SystemRDLParser#component_inst_elem.
    def exitComponent_inst_elem(self, ctx):
        anon = self.rule_names[ctx.parentCtx.getRuleIndex()] == 'anonymous_component_inst_elems'
        if anon:
            comp = self.curr_comp
            parent = self.curr_comp.parent
        else:  # if explicit_component_inst
            comp_name = ctx.parentCtx.getChild(
                0, SystemRDLParser.S_idContext).getText()
            comp = self.get_definition(Component.Component, comp_name)
            if comp is None:
                log.error('component \'{comp_name}\' definition not found', ctx.start.line)
            parent = self.curr_comp
        comp_type = comp.get_type()

        comp.inst_line = ctx.start.line
        is_array = False
        # instatiation
        if ctx.array() is None:
            inst = comp if anon else comp.customcopy()
            # set fieldwidth/signalwidth to 1 when no width specified
            if comp_type in ['Field', 'Signal']:
                inst = comp if anon else comp.customcopy()
                width = {'Field': 'fieldwidth',
                         'Signal': 'signalwidth'}[comp_type]
                inst.set_property(width, 1, ctx.start.line, [], False)
        else:
            indctx = ctx.getChild(1).getChild
            # array indices
            if ctx.getChild(1).getChild(2).getText() == ':':
                # (5.1.2.a.3.ii)
                if comp_type != 'Field':  # Signal too??
                    log.error('array indices not allowed for {comp_type}', ctx.start.line)
                left = extract_num(indctx(1).getText(), indctx(1).start.line)
                right = extract_num(indctx(3).getText(), indctx(3).start.line)
                if not isinstance(left, int) or not isinstance(right, int):
                    log.error('array indices should be unsizedNumeric', ctx.start.line)
                inst = comp if anon else comp.customcopy()
                inst.position = (left, right)
                inst.set_property('fieldwidth', abs(left-right)+1, ctx.start.line, [], False)
            # array declaration
            else:
                size = extract_num(indctx(1).getText(), indctx(1).start.line)
                if not isinstance(size, int):
                    log.error('array size should be unsizedNumeric', ctx.start.line)
                if comp_type in ['Field', 'Signal']:
                    inst = comp if anon else comp.customcopy()
                    width = {'Field': 'fieldwidth',
                             'Signal': 'signalwidth'}[comp_type]
                    inst.set_property(width, size, ctx.start.line, [], False)
                else:
                    inst0 = [comp if anon else comp.customcopy()]
                    inst = inst0 + [comp.customcopy() for _ in range(size - 1)]
                    is_array = True
        inst_id = ctx.getChild(0).getText()
        # iterate through insts and set parent, name and line
        for i in itercomp(inst):
            i.inst_id = inst_id
            i.parent = parent
            if i.name is None:
                i.name = inst_id
            i.line = ctx.start.line
            if comp_type == 'AddrMap':
                i.instantiated = True
        # set list_index for arrays
        if isinstance(inst, list):
            for i, instl in enumerate(inst):
                instl.list_index = i
        # set properties set with instatiation
        for prop in ['reset', 'at_addr', 'inc_addr', 'align_addr']:
            value = self.get_post_inst_prop_value(ctx, prop)
            if value is not None:
                if prop == 'inc_addr' and not is_array:
                    log.error('+= address stride is applicable only for arrays', ctx.start.line)
                for x in itercomp(inst):
                    x.set_property(prop, value, ctx.start.line, [], None)
        # set field position
        if comp_type == 'Field':
            # if parent has no bit order, infer it
            if parent.bit_order is None:
                if inst.position == (None, None) or inst.position[0] == inst.position[1]:
                    inst.bit_order = 'lsb0'
                    log.info('bit order set to default \'lsb0\'', ctx.start.line)
                else:
                    inst.bit_order = 'msb0' if inst.position[0] < inst.position[1] else 'lsb0'
                # propagate bit order up
                parent.bit_order = inst.bit_order
                temp = parent
                while temp.parent is not None:
                    temp.parent.bit_order = temp.bit_order
                    temp = temp.parent
            # set position if not explicitly specified
            if inst.position == (None, None):
                if len(parent.comps) == 0:
                    last_index = -1 if parent.bit_order == 'lsb0' else parent.regwidth
                else:
                    last_index = parent.comps[-1].position[0]
                if parent.bit_order == 'lsb0':
                    inst.position = (last_index + inst.fieldwidth, last_index + 1)
                else:
                    inst.position = (last_index - inst.fieldwidth, last_index - 1)
            else:
                if ((inst.position[0] > inst.position[1] and parent.bit_order == 'msb0') or
                        (inst.position[0] < inst.position[1] and parent.bit_order == 'lsb0')):
                    log.error('field bit order do not match register bit order', ctx.start.line)
            if max(inst.position) >= parent.regwidth or min(inst.position) < 0:
                log.error('field position out of range of register width', ctx.start.line)
            # check for overlapping fields
            if parent.filled_bits & set(range(min(inst.position), max(inst.position) + 1)):
                log.error('field position overlaps with a previous field', ctx.start.line)
            parent.filled_bits |= set(range(min(inst.position), max(inst.position) + 1))
        # if in root, component is signal
        if parent is None:
            self.add_root_sig_inst(inst, ctx.start.line)
        else:
            parent.add_comp(inst, ctx.start.line)
        # add to scoped insts for rhs reference
        if anon:
            self.scoped_insts[-2].append(inst)
        else:
            self.scoped_insts[-1].append(inst)

    # Enter a parse tree produced by SystemRDLParser#explicit_property_assign.
    def enterExplicit_property_assign(self, ctx):
        if self.rule_names[ctx.parentCtx.getRuleIndex()] == 'default_property_assign':
            if ctx.property_modifier():
                log.error('property modifier not allowed in default', ctx.start.line)
            prop = ctx.getChild(0).getText()
            if prop in ('name', 'desc'):
                if (ctx.property_assign_rhs() is None
                        or ctx.getChild(2).property_rvalue_constant() is None
                        or ctx.getChild(2).getChild(0).string() is None):
                    log.error(f'{prop} expected string value.', ctx.start.line)
                value = ctx.getChild(2).getText()
            else:
                def prop_class(prop):
                    for key, cls in self.COMPONENT_CLASS.items():
                        if prop in cls(None, None, [], [], None).properties:
                            return cls(None, None, [], [], None)
                    return None

                cls = prop_class(prop)
                if cls is None:
                    log.error(f'{prop} is not a builtin property.', ctx.start.line)
                if ctx.property_assign_rhs() is None:
                    value = True
                else:
                    value = self.extract_rhs_value(ctx.getChild(2), prop)
                if not cls.check_type(prop, value, ctx.start.line):
                    log.error(f'{prop} expected {cls.properties[prop]}.', ctx.start.line)
            self.add_default((prop, value), ctx.start.line)
        else:
            comp = self.curr_comp
            if ctx.property_modifier():
                if ctx.getChild(1).getText() != 'intr' or comp.get_type() != 'Field':
                    log.error('property modifier is allowed only for\'intr\' on Field', ctx.start.line)
                self.check_property_already_set(comp, 'intr', ctx.start.line)
                comp.set_property('intrmod', ctx.getChild(0).getText(),
                                  ctx.start.line, [], False)  # fix nonsticky
                comp.set_property('intr', True, ctx.start.line, [], False)
            else:
                prop = ctx.getChild(0).getText()
                if ctx.property_assign_rhs() is None:
                    value = self.get_implicit_value(
                        ctx.getChild(0))
                else:
                    value = self.extract_rhs_value(ctx.getChild(2), prop)
                self.check_property_already_set(comp, prop, ctx.start.line)
                comp.set_property(
                    prop, value, ctx.start.line, self.user_def_props, False)

    # Enter a parse tree produced by SystemRDLParser#post_property_assign.
    def enterPost_property_assign(self, ctx):
        inst, prop = self.extract_instance_ref(ctx.getChild(0))
        if prop is None:
            log.error('property is not specified.', ctx.start.line)
        if ctx.property_assign_rhs() is None:
            value = self.get_implicit_value(
                ctx.getChild(0).getChild(0, SystemRDLParser.S_propertyContext))
        else:
            value = self.extract_rhs_value(ctx.getChild(2), prop)
        self.check_property_already_set(inst, prop, ctx.start.line)
        for x in itercomp(inst):
            x.set_property(prop, value, ctx.start.line, self.user_def_props, True)

    # Enter a parse tree produced by SystemRDLParser#enum_def.
    def enterEnum_def(self, ctx):
        enum = Component.Enum(ctx.getChild(1).getText())
        self.extract_enum_body(ctx.getChild(2), enum)
        self.add_definition(enum, ctx.start.line)
