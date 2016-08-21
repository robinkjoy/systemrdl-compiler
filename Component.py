from copy import deepcopy


def is_power_2(number):
    return number > 0 and (number & (number - 1)) == 0

def true_or_assigned(val):
    if val is None or val == '' or (isinstance(val, bool) and not val):
        return 0
    else:
        return 1


class Component:

    UNIVERSAL_PROPERTIES = {
        'name': 'string',
        'desc': 'string'
        }
    PROPERTIES = {}
    NON_DYNAMIC_PROPERTIES = []
    EXCLUSIVES = [[]]

    def __init__(self, def_id, inst_id, parent):
        self.def_id = def_id
        self.inst_id = inst_id
        self.name = inst_id
        self.parent = parent
        self.desc = ''
        self.comps = []
        for prop in self.PROPERTIES:
            setattr(self, prop, self.get_default(prop))
        self.PROPERTIES.update(self.UNIVERSAL_PROPERTIES)

    def get_type(self):
        return self.__class__.__name__

    def set_property(self, prop, value, user_def_props, is_dynamic):
        value = self.validate_property(prop, value, user_def_props, is_dynamic)
        setattr(self, prop, value)
        self.validate_exclusivity()

    def get_default(self, prop):
        prop_default = {
            'boolean': False,
            'string': '',
            'numeric': None,
            'sizedNumeric': None,
            'unsizedNumeric': None,
            'accessType': 'rw',
            'addressingType': 'realign',
            'precedenceType': 'sw',
            'reference': None,
            'reference2enum': None,
            'ComponentType': [],
            'proptypeType': None,
            'defaultValue': None
            }
        prop_type = self.PROPERTIES[prop]
        if isinstance(prop_type, list):
            prop_type = prop_type[0]
        return prop_default[prop_type]

    def check_type(self, prop, value):
        prop_types = self.PROPERTIES[prop]
        if isinstance(prop_types, str):
            prop_types = [prop_types]
        for prop_type in prop_types:
            if prop_type == 'boolean' and isinstance(value, bool):
                return True
            elif prop_type == 'string' and isinstance(value, str):
                return True
            elif prop_type in ('numeric', 'unsizedNumeric') and isinstance(value, int):
                return True
            elif prop_type == 'sizedNumeric' and isinstance(value, tuple):
                return True
            elif prop_type == 'accessType' and value in ('rw', 'wr', 'r', 'w', 'na'):
                return True
            elif prop_type == 'addressingType' and value in ('compact', 'realign', 'fullalign'):
                return True
            elif prop_type == 'precedenceType' and value in ('sw', 'hw'):
                return True
            elif prop_type == 'reference':
                # not implemented
                print('reference properties not implemented')
                return True
            elif prop_type == 'ComponentType' and value[0] in ('field', 'reg', 'regfile', 'addrmap', 'all'):
                return True
            elif prop_type == 'proptypeType' and value in ('string', 'number', 'boolean', 'ref'):
                return True
            elif prop_type == 'defaultValue':
                if getattr(self, 'proptype', None) is None:
                    return False
                elif self.proptype == 'string':
                    return isinstance(value, str)
                elif self.proptype == 'number':
                    return isinstance(value, int) or isinstance(value, tuple)
                elif self.proptype == 'boolean':
                    return isinstance(value, bool)
                elif self.proptype == 'ref':
                    print('reference properties not implemented')
                    return True
        return False

    def validate_property(self, prop, value, user_def_props, is_dynamic):
        if prop in self.PROPERTIES:
            if is_dynamic and prop in self.NON_DYNAMIC_PROPERTIES:
                exit('Error: Property \'{}\' cannot be assigned dynamically.'.format(prop))
            if not self.check_type(prop, value):
                exit('Error: Property \'{}\' expected {}.'.format(prop, self.PROPERTIES[prop]))
        else:
            user_def_prop_type = {
                'number': ['numeric', 'sizedNumeric'],
                'string': 'string',
                'boolean': 'boolean',
                'ref': 'reference'
                }
            user_def_prop = [x for x in user_def_props if x.def_id == prop]
            if not user_def_prop:
                exit('Error: Property \'{}\' not defined for {}.'.format(prop, self.get_type()))
            else:
                self.PROPERTIES[prop] = user_def_prop_type[user_def_prop[0].proptype]
                if value is None:
                    value = user_def_prop[0].default
                elif not self.check_type(prop, value):
                    exit('Error: Property \'{}\' expected {}.'.format(prop, self.PROPERTIES[prop]))
        return value

    def validate_exclusivity(self):
        for exs in self.EXCLUSIVES:
            if sum(map(true_or_assigned, [getattr(self, ex) for ex in exs])) > 1:
                exit('Error: Properties {} should be exclusive in {}'.format(', '.join(exs),
                                                                            self.get_type()))

    def customcopy(self):
        # don't copy references to other components, except child Components
        memo = {id(self.parent): self.parent}
        for prop in self.PROPERTIES:
            prop_value = getattr(self, prop)
            if isinstance(prop_value, Component):
                memo.update({id(prop_value): prop_value})
        return deepcopy(self, memo)

    def add_comp(self, inst):
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
            exit('error: {} instance not allowed in {}'.format(comp_type, parent_type))
        inst_id = inst[0].inst_id if isinstance(inst, list) else inst.inst_id
        if any([x for x in self.comps if (isinstance(x, list) and x[0].inst_id == inst_id)
            or (isinstance(x, Component) and x.inst_id == inst_id)]):
            exit('error: all instance names should be unique within a scope')
        self.comps.append(inst)

    def pprint(self, level=0):
        indent = 4
        print(' '*level*indent+'{} {} {} {{'.format(self.get_type(), self.def_id, self.inst_id))
        max_len = len(max(self.PROPERTIES, key=len))
        for prop in self.PROPERTIES:
            value = getattr(self, prop)
            if not true_or_assigned(value):
                continue
            print('{}{}{:{}} = {}'.format(' '*level*indent, ' '*indent, prop, max_len, value))
        for comp in self.comps:
            if isinstance(comp, list):
                print(' '*(level+1)*indent+'[')
                for c in comp:
                    c.pprint(level+2)
                print(' '*(level+1)*indent+']')
            else:
                comp.pprint(level+1)
        print(' '*level*indent+'}')

class AddrMap(Component):

    PROPERTIES = {
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
        'arbiter': 'string'
        }
    NON_DYNAMIC_PROPERTIES = ['alignment', 'sharedextbus', 'addressing',
            'rsvdset', 'rsvdsetX', 'msb0', 'lsb0', 'bridge', 'arbiter']
    EXCLUSIVES = [['msb0', 'lsb0']] # (10.3.1.g)

    def __init__(self, def_id, inst_id, parent):
        super().__init__(def_id, inst_id, parent)
        self.instantiated = False

    def set_property(self, prop, value, user_def_props, is_dynamic=False):
        super().set_property(prop, value, user_def_props, is_dynamic)
        # semantics (10.3.1)
        if prop == 'alignment' and not is_power_2(value):
            exit('Error: Property \'alignment\' should be a power of two.')

class RegFile(Component):

    PROPERTIES = {
        'alignment': 'unsizedNumeric',
        'sharedextbus': 'boolean',
        # Instance properties
        'at_addr': 'unsizedNumeric',
        'inc_addr': 'unsizedNumeric',
        'align_addr': 'unsizedNumeric'
        }
    NON_DYNAMIC_PROPERTIES = ['alignment', 'sharedextbus']
    EXCLUSIVES = [['at_addr', 'align_addr']]    # (9.1.1.h)

    def set_property(self, prop, value, user_def_props, is_dynamic=False):
        super().set_property(prop, value, user_def_props, is_dynamic)
        # semantics (9.1.1)
        if prop == 'alignment' and not is_power_2(value):
            exit('Error: Property \'alignment\' should be a power of two.')

class Register(Component):

    PROPERTIES = {
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
    NON_DYNAMIC_PROPERTIES = ['regwidth', 'shared']
    EXCLUSIVES = [['at_addr', 'align_addr']]    # (9.1.1.h)

    def set_property(self, prop, value, user_def_props, is_dynamic=False):
        # semantics (8.5.1)
        if prop in ('regwidth', 'accesswidth') and ( not is_power_2(value) or value < 8 ):
            exit('Error: Property \'{}\' should be a power of two and >= 8.'.format(prop))
        if (prop in ('at_addr', 'inc_addr', 'align_addr')
                and self.parent.get_type() != 'RegFile'):
            exit('error: address allocation is valid only for reg/regfiles inside regfile')
        super().set_property(prop, value, user_def_props, is_dynamic)
        # if self.accesswidth > self.regwidth:
        #     exit('Error: \'accesswidth\' should not exceed \'regwidth\'.')

class Field(Component):

    PROPERTIES = {
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
        # Interrupt types
        'posedge': 'boolean',
        'negedge': 'boolean',
        'bothedge': 'boolean',
        'level': 'boolean',
        'nonsticky': 'boolean',
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
    NON_DYNAMIC_PROPERTIES = ['hw', 'fieldwidth']
    EXCLUSIVES = [
        ['rclr', 'rset'],
        ['woset', 'woclr'],
        ['swwe', 'swwel'],
        ['we', 'wel'],                              # (7.7.1.c)
        ['hwenable', 'hwmask'],                     # (7.7.1.d)
        ['incrwidth', 'incrvalue'],                 # (7.8.2.1.a)
        ['decrwidth', 'decrvalue'],                 # (7.8.2.1.b)
        ['enable', 'mask'],                         # (7.9.1.a)
        ['haltenable', 'haltmask'],                 # (7.9.1.b)
        ['nonsticky', 'sticky', 'stickybit'],       # (7.9.1.c)
        ['posedge', 'negedge', 'bothedge', 'level'] # (7.9.1.g)
        ]

    def __init__(self, def_id, inst_id, parent):
        super().__init__(def_id, inst_id, parent)
        self.position = (None, None)
        self.size = None

    def set_property(self, prop, value, user_def_props, is_dynamic=False):
        if prop == 'reset' and isinstance(value, int) and value != 0:
            exit('Error: Verilog style integer should be used for non-zero reset values.')  # (7.5.1.a)
        super().set_property(prop, value, user_def_props, is_dynamic)
        invalid_accesses = [('w', 'w'), ('w', 'na'), ('na', 'w'), ('na', 'na')] # check after completion??
        if prop in ('sw', 'hw') and (self.sw, self.hw) in invalid_accesses:                 # (Table 9)
            exit('Error: Invalid field access pair.')

class Signal(Component):

    PROPERTIES = {
        'signalwidth': 'numeric',
        'sync': 'boolean',
        'async': 'boolean',
        'cpuif_reset': 'boolean',
        'field_reset': 'boolean',
        'activelow': 'boolean',
        'activehigh': 'boolean'
        }
    NON_DYNAMIC_PROPERTIES = ['signalwidth']
    EXCLUSIVES = [['sync', 'async'], ['activehigh', 'activelow']]

    def __init__(self, def_id, inst_id, parent):
        super().__init__(def_id, inst_id, parent)
        self.size = None

class Enum(Component):

    def __init__(self, def_id):
        super().__init__(def_id, None, None)

    def set_property(self, prop, value):
        super().set_property(prop, value, [], False)

class EnumEntry(Component):

    PROPERTIES = {'value': 'sizedNumeric'}

    def __init__(self, def_id, parent):
        super().__init__(def_id, None, parent)
        self.value = None

    def set_property(self, prop, value):
        super().set_property(prop, value, [], False)

class Property(Component):

    PROPERTIES = {
        'component': 'ComponentType',
        'proptype': 'proptypeType',
        'default': 'defaultValue'
        }

    def __init__(self, def_id):
        super().__init__(def_id, None, None)

    def set_property(self, prop, value):
        if prop == 'component':
            value = [value] + getattr(self, 'component')
        super().set_property(prop, value, [], False)
