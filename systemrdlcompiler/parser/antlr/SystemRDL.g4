/*
The following code is an extension of the SystemRDL 1.0 grammar provided for use by Accellera under Apache 2.0 license.  
See http://accellera.org/downloads/standards/systemrdl for additional info.
*/

grammar SystemRDL;

tokens  { INST_ID, PROPERTY }

root
  : ( component_def
    | enum_def
    | explicit_component_inst
    | property_assign
    | property_definition
    )* EOF
  ;

 property_definition
   : 'property'
     s_id
     LBRACE
     property_body
     RBRACE
     SEMI
   ;

property_body
  :
   ( property_type | property_usage | property_default )*
  ;

property_type
  :
    'type' EQ
    ( property_string_type
    | property_number_type
    | property_boolean_type
    | property_ref_type
    ) SEMI
  ;

property_default
  :
    (
    'default' EQ (string | num | 'true' | 'false')
    SEMI
    )
  ;

property_usage
  :
    'component' EQ property_component (OR property_component)* SEMI
  ;

property_component
  : ('signal' | 'addrmap' | 'reg' | 'regfile' | 'field' | 'all')
  ;

property_boolean_type
  : 'boolean'
  ;

property_string_type
  : 'string'
  ;

property_number_type
  : 'number'
  ;

property_ref_type
  : ('addrmap' | 'reg' | 'regfile' | 'field' | 'ref')
  ;

component_def
  : ( 'addrmap' | 'regfile' | 'reg' | 'field' | 'signal' )
    ( s_id
    |
    )
    LBRACE
      ( component_def
      | explicit_component_inst
      | property_assign
      | enum_def
      )*
    RBRACE
    ( anonymous_component_inst_elems )?
    SEMI
  ;

explicit_component_inst
  : ( 'external' )?
    ( 'internal' )?
    ( 'alias' s_id )?
    s_id
    component_inst_elem
    (COMMA component_inst_elem)*
    SEMI
  ;

anonymous_component_inst_elems
  : ('external')?               //?? not in spec
    component_inst_elem
    (COMMA component_inst_elem)*
  ;

component_inst_elem
  : s_id
    (array)?
    (EQ  num)?   // reset
    (AT  num)?   // address
    (INC num)? //addr inc
    (MOD num)?  //addr mod
  ;

array
  : LSQ num
    (COLON num)?
    RSQ
  ;

instance_ref
  : instance_ref_elem
    (DOT instance_ref_elem)*
    ( DREF s_property )?
  ;

instance_ref_elem
  : s_id
    (LSQ num RSQ)?
  ;

property_assign
  : default_property_assign SEMI
  | explicit_property_assign SEMI
  | post_property_assign SEMI
  ;

default_property_assign
  : 'default'
    explicit_property_assign
  ;

explicit_property_assign
  : property_modifier       // nonsticky can be used with others
    s_property              // change??

  | s_property
    ( EQ property_assign_rhs )?
  ;

post_property_assign
  : instance_ref
    ( EQ property_assign_rhs )?
  ;

property_assign_rhs
  : property_rvalue_constant
  | 'enum' enum_body
  | instance_ref
  | concat
  ;

concat
  : LBRACE
    concat_elem
    (COMMA concat_elem)*
    RBRACE
  ;

concat_elem
  : instance_ref
  | num
  ;

s_property
  : 'name'
  | 'desc'
  | 'arbiter'
  | 'rset'
  | 'rclr'
  | 'woclr'
  | 'woset'

  | 'we'
  | 'wel'

  | 'swwe'
  | 'swwel'

  | 'hwset'
  | 'hwclr'

  | 'swmod'
  | 'swacc'

  | 'sticky'
  | 'stickybit'
  | 'intr'

  | 'anded'
  | 'ored'
  | 'xored'

  | 'counter'
  | 'overflow'

  | 'sharedextbus'
  | 'errextbus'

  | 'reset'

  | 'littleendian'
  | 'bigendian'
  | 'rsvdset'
  | 'rsvdsetX'
  | 'bridge'
  | 'shared'
  | 'msb0'
  | 'lsb0'
  | 'sync'
  | 'async'
  | 'cpuif_reset'
  | 'field_reset'
  | 'activehigh'
  | 'activelow'
  | 'singlepulse'
  | 'underflow'

  | 'incr'
  | 'decr'

  | 'incrwidth'
  | 'decrwidth'

  | 'incrvalue'
  | 'decrvalue'

  | 'saturate'
  | 'decrsaturate'

  | 'threshold'
  | 'decrthreshold'

  | 'dontcompare'
  | 'donttest'
  | 'internal'

  | 'alignment'
  | 'regwidth'
  | 'fieldwidth'
  | 'signalwidth'
  | 'accesswidth'


  | 'sw'
  | 'hw'
  | 'addressing'
  | 'precedence'

  | 'encode'
  | 'resetsignal'
  | 'clock'

  | 'mask'
  | 'enable'

  | 'hwenable'
  | 'hwmask'

  | 'haltmask'
  | 'haltenable'


  | 'halt'

  | 'next'

//  | PROPERTY  ??
  | s_id
  ;

property_rvalue_constant
  : 'true'
  | 'false'

  | 'rw'
  | 'wr'
  | 'r'
  | 'w'
  | 'na'

  | 'compact'
  | 'regalign'
  | 'fullalign'

  | 'hw'
  | 'sw'

  | num
  | string
  ;

property_modifier
  : 'posedge'
  | 'negedge'
  | 'bothedge'
  | 'level'
  | 'nonsticky'
  ;

s_id
  : ID
  | INST_ID
  ;

num
  : NUM
  ;

string
  : STR
  ;

enum_def
  : 'enum' s_id
    enum_body
    SEMI
  ;

enum_body
  : LBRACE (enum_entry)* RBRACE
  ;

enum_entry
  : s_id
    (EQ num)?
    ( LBRACE (enum_property_assign)* RBRACE )?
    SEMI
  ;

enum_property_assign
  : ( 'name'
    | 'desc'
    )
    EQ string
    SEMI
  ;

fragment LETTER : ('a'..'z'|'A'..'Z') ;

WS :
  [ \t\r\n]+ -> skip
  ;

COMMENT
  : '/*' .*? '*/' -> skip
  ;
LINE_COMMENT
  : '//' ~[\r\n]* -> skip
  ;
ID
  : ('\\')?
    (LETTER | '_')(LETTER | '_' | '0'..'9')*
  ;

fragment VNUM
  : '\'' ( 'b' ('0' | '1' | '_')+
         | 'd' ('0'..'9' | '_')+
         | 'o' ('0'..'7' | '_')+
         | 'h' ('0'..'9' | 'a'..'f' | 'A'..'F' | '_')+
         )
  ;

NUM
  : ('0'..'9')* (VNUM | ('0'..'9'))
  | '0x' ('0'..'9' | 'a'..'f' | 'A'..'F')+
  ;

fragment ESC_DQUOTE
  : '\\"'
  ;

STR
  : '"'
      ( ~('"' | '\n' | '\\')
      | ESC_DQUOTE
      | '\n'
      )*
    '"' // "
  ;

LBRACE : '{' ;
RBRACE : '}' ;
LSQ    : '[' ;
RSQ    : ']' ;

LPAREN : '(' ;
RPAREN : ')' ;

AT     : '@' ;
OR     : '|' ;
SEMI   : ';' ;
COLON  : ':' ;
COMMA  : ',' ;
DOT    : '.' ;

DREF   : '->';

EQ     : '=' ;
INC    : '+=';
MOD    : '%=';

