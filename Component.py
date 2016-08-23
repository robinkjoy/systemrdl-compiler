from copy import copy


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

    def __init__(self, def_id, inst_id, parent, defaults):
        self.def_id = def_id
        self.inst_id = inst_id
        self.parent = parent
        self.comps = []
        self.properties.update(self.UNIVERSAL_PROPERTIES)
        for prop in self.properties:
            setattr(self, prop, self.get_default(prop, defaults))

    def get_type(self):
        return self.__class__.__name__

    def set_property(self, prop, value, user_def_props, is_dynamic):
        self.validate_property(prop, value, user_def_props, is_dynamic)
        setattr(self, prop, value)
        self.validate_exclusivity()

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
        prop_default = {
            'boolean': False,
            'string': '""',
            'numeric': None,
            'sizedNumeric': None,
            'unsizedNumeric': None,
            'accessType': 'rw',
            'addressingType': 'realign',
            'precedenceType': 'sw',
            'reference': None,
            'reference2enum': None
            }
        prop_type = self.properties[prop]
        if isinstance(prop_type, list):
            prop_type = prop_type[0]
        return prop_default[prop_type]

    def check_type(self, prop, value):
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
            elif prop_type == 'addressingType' and value in ('compact', 'realign', 'fullalign'):
                return True
            elif prop_type == 'precedenceType' and value in ('sw', 'hw'):
                return True
            elif prop_type == 'reference' and isinstance(value, Component):
                return True
            elif prop_type == 'reference2enum' and isinstance(value, Enum):
                return True
        return False

    def validate_property(self, prop, value, user_def_props, is_dynamic):
        if prop in self.properties:
            if is_dynamic and prop in self.NON_DYNAMIC_PROPERTIES:
                exit('Error: Property \'{}\' cannot be assigned dynamically.'.format(prop))
            if not self.check_type(prop, value):
                exit('Error: Property \'{}\' expected {}.'.format(prop, self.properties[prop]))
        else:
            user_def_prop_type = {
                'number': ['numeric', 'sizedNumeric'],
                'string': 'string',
                'boolean': 'boolean',
                'ref': 'reference'
                }
            user_def_prop = [x for x in user_def_props if x.prop_id == prop]
            if not user_def_prop:
                exit('Error: Property \'{}\' not defined for {}.'.format(prop, self.get_type()))
            else:
                self.properties[prop] = user_def_prop_type[user_def_prop.prop_type]
                if value is None:
                    value = user_def_prop.prop_default
                elif not self.check_type(prop, value):
                    exit('Error: Property \'{}\' expected {}.'.format(prop, self.properties[prop]))

    def validate_exclusivity(self):
        for exs in self.EXCLUSIVES:
            if sum(map(true_or_assigned, [getattr(self, ex) for ex in exs])) > 1:
                exit('Error: Properties {} should be exclusive in {}'.format(', '.join(exs),
                                                                            self.get_type()))

    def customcopy(self):
        if isinstance(self, Signal) or isinstance(self, Enum):
            return self
        newcopy = copy(self)
        def copy_method(x):
            return [y.customcopy() for y in x] if isinstance(x, list) else x.customcopy()
        newcopy.comps = [copy_method(x) for x in self.comps]
        return newcopy

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
        max_len = len(max(self.properties, key=len))
        for prop in self.properties:
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

    NON_DYNAMIC_PROPERTIES = ['alignment', 'sharedextbus', 'addressing',
            'rsvdset', 'rsvdsetX', 'msb0', 'lsb0', 'bridge', 'arbiter']
    EXCLUSIVES = [['msb0', 'lsb0']] # (10.3.1.g)

    def __init__(self, def_id, inst_id, parent, defaults):
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
            'arbiter': 'string'
            }
        super().__init__(def_id, inst_id, parent, defaults)
        self.instantiated = False

    def check_type(self, prop, value):
        if not super().check_type(prop, value):
            return False
        # semantics (10.3.1)
        if prop == 'alignment' and not is_power_2(value):
            exit('Error: Property \'alignment\' should be a power of two.')
        return True

class RegFile(Component):

    NON_DYNAMIC_PROPERTIES = ['alignment', 'sharedextbus']
    EXCLUSIVES = [['at_addr', 'align_addr']]    # (9.1.1.h)

    def __init__(self, def_id, inst_id, parent, defaults):
        self.properties = {
            'alignment': 'unsizedNumeric',
            'sharedextbus': 'boolean',
            # Instance properties
            'at_addr': 'unsizedNumeric',
            'inc_addr': 'unsizedNumeric',
            'align_addr': 'unsizedNumeric'
            }
        super().__init__(def_id, inst_id, parent, defaults)


    def check_type(self, prop, value):
        if not super().check_type(prop, value):
            return False
        # semantics (9.1.1)
        if prop == 'alignment' and not is_power_2(value):
            exit('Error: Property \'alignment\' should be a power of two.')
        return True

class Register(Component):

    NON_DYNAMIC_PROPERTIES = ['regwidth', 'shared']
    EXCLUSIVES = [['at_addr', 'align_addr']]    # (9.1.1.h)

    def __init__(self, def_id, inst_id, parent, defaults):
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
        super().__init__(def_id, inst_id, parent, defaults)

    def check_type(self, prop, value):
        if not super().check_type(prop, value):
            return False
        # semantics (8.5.1)
        if prop in ('regwidth', 'accesswidth') and ( not is_power_2(value) or value < 8 ):
            exit('Error: Property \'{}\' should be a power of two and >= 8.'.format(prop))
        if (prop in ('at_addr', 'inc_addr', 'align_addr')
                and self.parent.get_type() != 'RegFile'):
            exit('error: address allocation is valid only for reg/regfiles inside regfile')
        return True

class Field(Component):

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

    def __init__(self, def_id, inst_id, parent, defaults):
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
        super().__init__(def_id, inst_id, parent, defaults)
        self.position = (None, None)
        self.size = None

    def check_type(self, prop, value):
        if not super().check_type(prop, value):
            return False
        if prop == 'reset' and isinstance(value, int) and value != 0:
            exit('Error: Verilog style integer should be used for non-zero reset values.')  # (7.5.1.a)
        return True
        # invalid_accesses = [('w', 'w'), ('w', 'na'), ('na', 'w'), ('na', 'na')] # check after completion??
        # if prop in ('sw', 'hw') and (self.sw, self.hw) in invalid_accesses:                 # (Table 9)
        #     exit('Error: Invalid field access pair.')

class Signal(Component):

    NON_DYNAMIC_PROPERTIES = ['signalwidth']
    EXCLUSIVES = [['sync', 'async'], ['activehigh', 'activelow']]

    def __init__(self, def_id, inst_id, parent, defaults):
        self.properties = {
            'signalwidth': 'numeric',
            'sync': 'boolean',
            'async': 'boolean',
            'cpuif_reset': 'boolean',
            'field_reset': 'boolean',
            'activelow': 'boolean',
            'activehigh': 'boolean'
            }
        super().__init__(def_id, inst_id, parent, defaults)
        self.size = None

class Enum(Component):

    def __init__(self, def_id):
        self.properties = {}
        super().__init__(def_id, None, None, [])

    def set_property(self, prop, value):
        super().set_property(prop, value, [], False)

class EnumEntry(Component):

    def __init__(self, def_id, value):
        self.properties = {}
        super().__init__(def_id, None, None, [])
        self.value = value

    def set_property(self, prop, value):
        super().set_property(prop, value, [], False)

class Property():

    def __init__(self, prop_id, prop_type, prop_usage, prop_default):
        self.prop_id = prop_id
        self.prop_type = prop_type
        self.prop_usage = prop_usage
        self.prop_default = prop_default