import copy
import logging
from math import ceil

from Common import itercomps
from Common import itercomps0

log = logging.getLogger()


def is_power_2(number):
    return number > 0 and (number & (number - 1)) == 0


def true_or_assigned(val):
    if val is None or val == '""' or (isinstance(val, bool) and not val):
        return 0
    else:
        return 1


class Component:
    UNIVERSAL_PROPERTIES = {
        'name': 'string',
        'desc': 'string'
    }
    NON_DYNAMIC_PROPERTIES = []
    EXCLUSIVES = [[]]

    def __init__(self, def_id, inst_id, parent, defaults, line):
        self.def_id = def_id
        self.inst_id = inst_id
        self.parent = parent
        self.comps = []
        self.properties.update(self.UNIVERSAL_PROPERTIES)
        for prop in self.properties:
            setattr(self, prop, self.get_default(prop, defaults))
        self.line = line
        self.inst_line = line
        self.addr = 0
        self.list_index = None

    def get_type(self):
        return self.__class__.__name__

    def set_property(self, prop, value, line, user_def_props, is_dynamic):
        value = self.validate_property(prop, value, line, user_def_props, is_dynamic)
        setattr(self, prop, value)
        exc = [x for x in self.EXCLUSIVES if prop in x]
        if exc and sum(map(true_or_assigned, [getattr(self, x) for x in exc[0]])) > 1:
            log.error('Properties {} should be exclusive in {} {}', self.line,
                      ', '.join(exc), self.get_type(),
                      self.def_id if self.inst_id is None else self.inst_id)

    def get_default(self, prop, defaults):
        def get_default_value(prop, defaults):
            for defs in reversed(defaults):
                if prop in defs:
                    return defs[prop]
            return None

        value = get_default_value(prop, defaults)
        if value is not None:
            return value
        if prop == 'name':
            return self.inst_id
        if prop == 'regwidth':
            return 32
        prop_default = {
            'boolean': False,
            'string': '""',
            'numeric': None,
            'sizedNumeric': None,
            'unsizedNumeric': None,
            'accessType': 'rw',
            'addressingType': 'regalign',
            'precedenceType': 'sw',
            'reference': None,
            'reference2enum': None,
            'intrmodType': None
        }
        prop_type = self.properties[prop]
        if isinstance(prop_type, list):
            prop_type = prop_type[0]
        return prop_default[prop_type]

    def check_type(self, prop, value, line):
        prop_types = self.properties[prop]
        if isinstance(prop_types, str):
            prop_types = [prop_types]
        for prop_type in prop_types:
            if prop_type == 'boolean' and isinstance(value, bool):
                return True
            elif (prop_type == 'string' and isinstance(value, str)
                  and len(value) > 1 and value[0] == '"' and value[-1] == '"'):
                return True
            elif prop_type in ('numeric', 'unsizedNumeric') and isinstance(value, int):
                return True
            elif prop_type == 'sizedNumeric' and isinstance(value, tuple):
                return True
            elif prop_type == 'accessType' and value in ('rw', 'wr', 'r', 'w', 'na'):
                return True
            elif prop_type == 'addressingType' and value in ('compact', 'regalign', 'fullalign'):
                return True
            elif prop_type == 'precedenceType' and value in ('sw', 'hw'):
                return True
            elif prop_type == 'reference' and isinstance(value, Component):
                return True
            elif prop_type == 'reference2enum' and isinstance(value, Enum):
                return True
            elif (prop_type == 'intrmodType'
                  and value in ('nonsticky', 'posedge', 'negedge', 'bothedge', 'level')):
                return True
        return False

    def validate_property(self, prop, value, line, user_def_props, is_dynamic):
        if prop in self.properties:
            if is_dynamic and prop in self.NON_DYNAMIC_PROPERTIES:
                log.error(f'Property \'{prop}\' cannot be assigned dynamically.', line)
            if not self.check_type(prop, value, line):
                log.error(f'Property \'{prop}\' expected {self.properties[prop]}.', line)
            if prop in ('signalwidth', 'fieldwidth') and getattr(self, prop) not in (None, value):
                log.error('instantiation width does not match explicitly defined width.', line)
        else:
            user_def_prop_type = {
                'number': ['numeric', 'sizedNumeric'],
                'string': 'string',
                'boolean': 'boolean',
                'ref': 'reference'
            }
            user_def_prop = next((x for x in user_def_props if x.prop_id == prop), None)
            if user_def_prop is None:
                log.error(f'Property \'{prop}\' not defined for {self.get_type()}.', line)
            else:
                self.properties[prop] = user_def_prop_type[user_def_prop.prop_type]
                if value is None:
                    value = user_def_prop.prop_default
                elif not self.check_type(prop, value, line):
                    log.error(f'Property \'{prop}\' expected {self.properties[prop]}.', line)
        return value

    def customcopy(self):
        if isinstance(self, Signal) or isinstance(self, Enum):
            return self
        newcopy = copy.copy(self)

        def copy_method(x):
            return [y.customcopy() for y in x] if isinstance(x, list) else x.customcopy()

        newcopy.comps = [copy_method(x) for x in self.comps]
        for comp in itercomps(newcopy.comps):
            comp.parent = newcopy
        newcopy.properties = copy.deepcopy(self.properties)
        return newcopy

    def add_comp(self, inst, line):
        allowed_insts = {
            'Enum': ['EnumEntry'],
            'Signal': [],
            'Field': ['Signal'],
            'Register': ['Field', 'Signal'],
            'RegFile': ['RegFile', 'Register', 'Signal'],
            'AddrMap': ['AddrMap', 'RegFile', 'Register', 'Signal'],  # Signal?
        }
        if type(inst) == list:
            comp_type = inst[0].get_type()
        else:
            comp_type = inst.get_type()
        parent_type = self.get_type()
        if comp_type not in allowed_insts[parent_type]:
            log.error(f'{comp_type} instance not allowed in {parent_type}', line)
        inst_id = inst[0].inst_id if isinstance(inst, list) else inst.inst_id
        if any([x for x in itercomps0(self.comps) if x.inst_id == inst_id]):
            log.error(f'all instance names should be unique within a scope', line)
        self.comps.append(inst)

    def pprint(self, level=0):
        indent = 4
        print(' ' * level * indent + '{} {} {} {{'.format(self.get_type(), self.def_id, self.inst_id))
        max_len = len(max(self.properties, key=len))
        for prop in self.properties:
            value = getattr(self, prop)
            if not true_or_assigned(value):
                continue
            print(f"{' ' * level * indent}{' ' * indent}{prop:{max_len}} = {value}")
        for comp in self.comps:
            if isinstance(comp, list):
                print(' ' * (level + 1) * indent + '[')
                for c in comp:
                    c.pprint(level + 2)
                print(' ' * (level + 1) * indent + ']')
            else:
                comp.pprint(level + 1)
        print(' ' * level * indent + '}')

    def get_full_name(self):
        list_index_str = '' if self.list_index is None else '_' + str(self.list_index)
        if self.parent is None or self.parent.get_type() == 'AddrMap':
            return self.inst_id or self.def_id
        else:
            return self.parent.get_full_name() + '_' + self.inst_id + list_index_str

    def populate_addresses(self, start_addr, addr_mode, align=None, listi=0):
        def align_addr_to(addr, align):
            return ceil(addr / align) * align

        self.addr = start_addr
        if self.at_addr:
            self.addr = self.at_addr
        ialign = getattr(self, 'alignment', None) or align
        if ialign:
            self.addr = align_addr_to(self.addr, ialign // 8)
        iaddr_mode = getattr(self, 'addressing', None) or addr_mode
        if self.get_type() == 'Register' and iaddr_mode in ['regalign', 'fullalign']:
            self.addr = align_addr_to(self.addr, self.regwidth // 8)
        # alignment of an array instance specifies the alignment of the start of the array (only)
        # but if inc_addr is specified it recalculates array start and applies inc_addr
        if self.align_addr and (listi == 0 or self.inc_addr):
            self.addr = ceil(self.addr / self.align_addr) * self.align_addr
        if self.inc_addr:
            self.addr += self.inc_addr * listi
        curr_addr = self.addr
        if self.get_type() in ['AddrMap', 'RegFile']:
            for compl in self.comps:
                if isinstance(compl, list):
                    if compl[0].get_type() == 'Register' and iaddr_mode == 'fullalign':
                        lsize = len(compl) * compl[0].regwidth
                        lalign = 1 << (lsize - 1).bit_length()  # round up to next power of 2
                        curr_addr = align_addr_to(curr_addr, lalign // 8)
                    # if inc_addr, pass first element's addr for all array elements
                    currl_addr = curr_addr
                    for i, comp in enumerate(compl):
                        if comp.inc_addr:
                            curr_addr = comp.populate_addresses(currl_addr, iaddr_mode, ialign, i)
                        else:
                            curr_addr = comp.populate_addresses(curr_addr, iaddr_mode, ialign, i)
                elif compl.get_type() == 'Signal':
                    continue
                else:
                    curr_addr = compl.populate_addresses(curr_addr, iaddr_mode, ialign)
            return curr_addr
        elif self.get_type() == 'Register':
            return self.addr + self.regwidth // 8


class AddrMap(Component):
    NON_DYNAMIC_PROPERTIES = ['alignment', 'sharedextbus', 'addressing',
                              'rsvdset', 'rsvdsetX', 'msb0', 'lsb0',
                              'bridge', 'arbiter']
    EXCLUSIVES = [['msb0', 'lsb0'], ['at_addr', 'align_addr']]  # (10.3.1.g)

    def __init__(self, def_id, inst_id, parent, defaults, line):
        self.properties = {
            'alignment': 'unsizedNumeric',
            'sharedextbus': 'boolean',
            'bigendian': 'boolean',
            'littleendian': 'boolean',
            'addressing': 'addressingType',
            'rsvdset': 'boolean',
            'rsvdsetX': 'boolean',
            'msb0': 'boolean',
            'lsb0': 'boolean',
            'bridge': 'boolean',
            'arbiter': 'string',
            # Instance properties
            'at_addr': 'unsizedNumeric',
            'inc_addr': 'unsizedNumeric',
            'align_addr': 'unsizedNumeric'
        }
        super().__init__(def_id, inst_id, parent, defaults, line)
        self.instantiated = False
        self.bit_order = None

    def check_type(self, prop, value, line):
        if not super().check_type(prop, value, line):
            return False
        # semantics (10.3.1)
        if prop == 'alignment' and not is_power_2(value):
            log.error('Property \'alignment\' should be a power of two.', line)
        return True

    def set_property(self, prop, value, line, user_def_props, is_dynamic):
        super().set_property(prop, value, line, user_def_props, is_dynamic)
        if prop in ('msb0', 'lsb0') and value:
            if self.bit_order is not None and self.bit_order != prop:
                log.error('Properties msb0, lsb0 should be exclusive in AddrMap {}', line,
                          self.def_id if self.inst_id is None else self.inst_id)
            self.bit_order = prop

    def get_regs_iter(self):
        def comp_iter(comp):
            if isinstance(comp, list):
                for c in comp:
                    yield from comp_iter(c)
            elif comp.get_type() == 'RegFile':
                for c in comp.comps:
                    yield from comp_iter(c)
            elif comp.get_type() == 'Register':
                yield comp

        for comp in self.comps:
            yield from comp_iter(comp)

    def pprint(self, level=0):
        super().pprint(level)
        print(f"{' ' * level * 4}@{self.addr:x}")

    def validate_addresses(self):
        filled_addr = set()
        for reg in self.get_regs_iter():
            reg_addr = set(range(reg.addr, reg.addr + reg.regwidth // 8))
            if filled_addr & reg_addr:
                log.error(f'Address 0x{reg.addr:x} of register {reg.inst_id} already assigned', reg.line)
            filled_addr |= reg_addr
        return max(filled_addr)


class RegFile(Component):
    NON_DYNAMIC_PROPERTIES = ['alignment', 'sharedextbus']
    EXCLUSIVES = [['at_addr', 'align_addr']]  # (9.1.1.h)

    def __init__(self, def_id, inst_id, parent, defaults, line):
        self.properties = {
            'alignment': 'unsizedNumeric',
            'sharedextbus': 'boolean',
            # Instance properties
            'at_addr': 'unsizedNumeric',
            'inc_addr': 'unsizedNumeric',
            'align_addr': 'unsizedNumeric'
        }
        super().__init__(def_id, inst_id, parent, defaults, line)
        self.bit_order = None

    def check_type(self, prop, value, line):
        if not super().check_type(prop, value, line):
            return False
        # semantics (9.1.1)
        if prop == 'alignment' and not is_power_2(value):
            log.error('Property \'alignment\' should be a power of two.', line)
        return True

    def pprint(self, level=0):
        super().pprint(level)
        print(f"{' ' * level * 4}@{self.addr:x}")


class Register(Component):
    NON_DYNAMIC_PROPERTIES = ['regwidth', 'shared']
    EXCLUSIVES = [['at_addr', 'align_addr']]  # (9.1.1.h)

    def __init__(self, def_id, inst_id, parent, defaults, line):
        self.properties = {
            'regwidth': 'numeric',
            'accesswidth': 'numeric',
            'errextbus': 'numeric',
            'intr': 'reference',
            'halt': 'reference',
            'shared': 'boolean',
            # Instance properties
            'at_addr': 'unsizedNumeric',
            'inc_addr': 'unsizedNumeric',
            'align_addr': 'unsizedNumeric'
        }
        super().__init__(def_id, inst_id, parent, defaults, line)
        self.bit_order = None
        self.filled_bits = set()

    def check_type(self, prop, value, line):
        if not super().check_type(prop, value, line):
            return False
        # semantics (8.5.1)
        if prop in ('regwidth', 'accesswidth') and (not is_power_2(value) or value < 8):
            log.error('Property \'{}\' should be a power of two and >= 8.', line, prop)
        return True

    def pprint(self, level=0):
        super().pprint(level)
        print(f"{' ' * level * 4}@{self.addr:x}")


class Field(Component):
    NON_DYNAMIC_PROPERTIES = ['hw', 'fieldwidth']
    EXCLUSIVES = [
        ['rclr', 'rset'],
        ['woset', 'woclr'],
        ['swwe', 'swwel'],
        ['we', 'wel'],  # (7.7.1.c)
        ['hwenable', 'hwmask'],  # (7.7.1.d)
        ['incrwidth', 'incrvalue'],  # (7.8.2.1.a)
        ['decrwidth', 'decrvalue'],  # (7.8.2.1.b)
        ['enable', 'mask'],  # (7.9.1.a)
        ['haltenable', 'haltmask'],  # (7.9.1.b)
        ['nonsticky', 'sticky', 'stickybit'],  # (7.9.1.c)
    ]

    def __init__(self, def_id, inst_id, parent, defaults, line):
        self.properties = {
            # Field access properties
            'hw': 'accessType',
            'sw': 'accessType',
            # Hardware signal properties
            'next': 'reference',
            'reset': ['numeric', 'sizedNumeric', 'reference'],
            'resetsignal': 'reference',
            # Software access properties
            'rclr': 'boolean',
            'rset': 'boolean',
            'woset': 'boolean',
            'woclr': 'boolean',
            'swwe': ['boolean', 'reference'],
            'swwel': ['boolean', 'reference'],
            'swmod': ['boolean', 'reference'],
            'swacc': ['boolean', 'reference'],
            'singlepulse': 'boolean',
            # Hardware access properties
            'we': ['boolean', 'reference'],
            'wel': ['boolean', 'reference'],
            'anded': ['boolean', 'reference'],
            'ored': ['boolean', 'reference'],
            'xored': ['boolean', 'reference'],
            'fieldwidth': 'numeric',
            'hwclr': 'boolean',
            'hwset': 'boolean',
            'hwenable': 'sizedNumeric',
            'hwmask': 'sizedNumeric',
            # Counter field properties
            'counter': 'boolean',
            'threshold': ['boolean', 'reference'],
            'saturate': ['boolean', 'reference'],
            'incrthreshold': ['boolean', 'reference'],
            'incrsaturate': ['boolean', 'reference'],
            'overflow': 'reference',
            'underflow': 'reference',
            'incrvalue': ['boolean', 'reference'],
            'incr': 'reference',
            'incrwidth': 'numeric',
            'decrvalue': ['boolean', 'reference'],
            'decr': 'reference',
            'decrwidth': 'numeric',
            'decrthreshold': ['boolean', 'reference'],
            'decrsaturate': ['boolean', 'reference'],
            # Interrupt modifiers
            'nonsticky': 'boolean',
            'intrmod': 'intrmodType',
            # Field access interrupt properties
            'intr': 'boolean',
            'enable': 'reference',
            'mask': 'reference',
            'haltenable': 'reference',
            'haltmask': 'reference',
            'sticky': 'boolean',
            'stickybit': 'boolean',
            # Miscellaneous properties
            'encode': 'reference2enum',
            'precedence': 'precedenceType'
        }
        super().__init__(def_id, inst_id, parent, defaults, line)
        self.position = (None, None)

    def check_type(self, prop, value, line):
        if not super().check_type(prop, value, line):
            return False
        if prop == 'reset' and isinstance(value, int) and value != 0:
            log.error('Verilog style integer should be used for non-zero reset values.', line)  # (7.5.1.a)
        return True

    def set_property(self, prop, value, line, user_def_props, is_dynamic):
        super().set_property(prop, value, line, user_def_props, is_dynamic)
        invalid_accesses = [('w', 'w'), ('w', 'na'), ('na', 'w'), ('na', 'na')]
        if prop in ('sw', 'hw') and (self.sw, self.hw) in invalid_accesses:  # (Table 9)
            log.error('invalid field access pair in Field {}', self.line,
                      self.inst_id)
        # reset size
        if prop == 'reset' and self.fieldwidth is not None:
            if isinstance(self.reset, tuple) and self.reset[0] != self.fieldwidth:
                log.warning('reset width does not match fieldwidth in Field {}', self.line,
                            self.inst_id)
            if isinstance(self.reset, Signal) and self.reset.signalwidth != self.fieldwidth:
                log.warning('reset value signal width does not match fieldwidth in Field {}', self.line,
                            self.inst_id)

    def pprint(self, level=0):
        super().pprint(level)
        print(f"{' ' * level * 4}[{self.position[0]}:{self.position[1]}]")


class Signal(Component):
    NON_DYNAMIC_PROPERTIES = ['signalwidth']
    EXCLUSIVES = [['sync', 'async'], ['activehigh', 'activelow']]

    def __init__(self, def_id, inst_id, parent, defaults, line):
        self.properties = {
            'signalwidth': 'numeric',
            'sync': 'boolean',
            'async': 'boolean',
            'cpuif_reset': 'boolean',
            'field_reset': 'boolean',
            'activelow': 'boolean',
            'activehigh': 'boolean'
        }
        super().__init__(def_id, inst_id, parent, defaults, line)


class Enum(Component):

    def __init__(self, def_id):
        self.properties = {}
        super().__init__(def_id, None, None, [], None)

    def set_property(self, prop, value, line):
        super().set_property(prop, value, line, [], False)


class EnumEntry(Component):

    def __init__(self, def_id, value):
        self.properties = {}
        super().__init__(def_id, None, None, [], None)
        self.value = value

    def set_property(self, prop, value, line):
        super().set_property(prop, value, line, [], False)


class Property:

    def __init__(self, prop_id, prop_type, prop_usage, prop_default):
        self.prop_id = prop_id
        self.prop_type = prop_type
        self.prop_usage = prop_usage
        self.prop_default = prop_default
