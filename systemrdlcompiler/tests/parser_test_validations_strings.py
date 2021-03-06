test_strings = [
    # Listener.py
    # extract_num
    ("default reset=1'b10;", "ERROR:test(1):Number does not fit within specified bit width\n"),
    # add_definition
    ("reg rr {reg rr2{};};", "ERROR:test(1):Register definition not allowed in Register\n"),
    ("field rr{};field rr{};", "ERROR:test(1):all definition names should be unique within a scope\n"),
    # add_root_sig_inst
    ("signal {}ss; signal {}ss;", "ERROR:test(1):all instance names should be unique within a scope\n"),
    # add_default
    ("default sw = r;default sw = rw;", "ERROR:test(1):defaults can be assigned only once per scope\n"),
    # extract_rhs_value
    ("signal {}s1; field ff{anded=s1;ored=s1;};", "ERROR:test(1):signal s1 already driven\n"),
    ("field ff{reset={1'b1,1'b1};};", "ERROR:test(1):concat not implemented\n"),
    # extract_enum_body
    ("enum ee{};", "ERROR:test(1):no entries in enum\n"),
    ("enum ee{aa=1;};", "ERROR:test(1):enum entry value should be sizedNumeric\n"),
    ("enum ee{aa;aa;};", "ERROR:test(1):aa already defined in enum\n"),
    ("enum ee{aa=1'b1; bb;};", "ERROR:test(1):auto-assigned value 2 for bb do not fit in existing value size\n"),
    ("enum ee{aa=2'h0;ab=1'b1;};", "ERROR:test(1):size does not match others\n"),
    ("enum ee{aa=1'h0;ab=1'b0;};", "ERROR:test(1):1'b0 already defined in enum\n"),
    # extract_instance_ref
    ("addrmap am {reg {field {} ff;} rr[2];rr.ff->sw = r;};", "ERROR:test(1):array index for rr not specified\n"),
    ("ff->sw = r;", "ERROR:test(1):ff not found\n"),
    ("reg rr{field{}ff; ff[1]->we;};", "ERROR:test(1):ff is not an array\n"),
    ("regfile rf {reg {field{}ff;}rr[2];rr[2'd1]->sw=r;};", "ERROR:test(1):array index should be numeric\n"),
    ("regfile rf {reg {field{}ff;}rr[2];rr[2]->sw=r;};", "ERROR:test(1):array index out of range\n"),
    # extract_instance_ref_rhs
    ("field ff{reset=ss;};", "ERROR:test(1):ss not found\n"),
    ("regfile rf{ reg {field {}ff1;}rr1; reg {field {reset=rr1.ff2;}ff2;}rr2;};", "ERROR:test(1):ff2 not found\n"),
    ("signal {}ss; field ff{reset=ss[0];};", "ERROR:test(1):ss is not an array\n"),
    ("regfile rf{ reg {field {}ff1;}rr1[2]; reg {field {reset=rr1[1'b1].ff2;}ff2;}rr2;};",
        "ERROR:test(1):array index should be numeric\n"),
    ("regfile rf{ reg {field {}ff1;}rr1[2]; reg {field {reset=rr1[2].ff2;}ff2;}rr2;};",
        "ERROR:test(1):array index out of range\n"),
    ("regfile rf{ reg {field {}ff1;}rr1[2]; reg {field {reset=rr1.ff2;}ff2;}rr2;};",
        "ERROR:test(1):array index for rr1 not specified\n"),
    # check_property_already_set
    ("field ff{sw=r; sw=rw;};", "ERROR:test(1):property 'sw' already assigned in scope\n"),
    # exitRoot
    ("", "ERROR:test(1):No addressmaps found\n"),
    # enterProperty_body
    ("property fld_p {component = field;};", "ERROR:test(1):property type not specified\n"),
    ("property fld_p {type = string; component = field; type = string;};", "ERROR:test(1):property type reassigned\n"),
    ("property fld_p {type = string;};", "ERROR:test(1):property component not specified\n"),
    ("property fld_p {component = field; type = string;component = field;};",
     "ERROR:test(1):property component reassigned\n"),
    ("property fld_p {component = field; type = string;default=\"a\";default=\"a\";};",
     "ERROR:test(1):property default reassigned\n"),
    ("property fld_p {component = field; type = string; default = 1;};", "ERROR:test(1):default does not match type\n"),
    ("property fld_p {component = field; type = number; default = true;};",
     "ERROR:test(1):default does not match type\n"),
    ("property pp{component=field; type=number; default=1'b1;};",
     "ERROR:test(1):default value cannot be sizedNumeric\n"),
    ("property fld_p {component = field; type = boolean; default = \"true\";};",
     "ERROR:test(1):default does not match type\n"),
    # enterComponent_def
    ("field {}ff;", "ERROR:test(1):field should not be instantiated in root scope\n"),
    # exitComponent_def
    ("addrmap am {reg {};};", "ERROR:test(1):definition name or instantiation name not specified\n"),
    ("addrmap am {};", "ERROR:test(1):no child components in AddrMap\n"),
    # enterAnonymous_component_inst_elems
    ("addrmap am {}am;", "ERROR:test(1):both definition name and instantiation name specified\n"),
    # exitComponent_inst_elem
    ("ff ff1;", "ERROR:test(1):component 'ff' definition not found\n"),
    ("signal ss{}; ss ss1[2:0];", "ERROR:test(1):array indices not allowed for Signal\n"),
    ("field ff{}; ff ff1[1'b1:1'b0];", "ERROR:test(1):array indices should be unsizedNumeric\n"),
    ("reg rr{field {}ff;}; rr rr1[1'b1];", "ERROR:test(1):array size should be unsizedNumeric\n"),
    ("field ff{}; ff ff1 += 0x4;", "ERROR:test(1):+= address stride is applicable only for arrays\n"),
    ("field ff{field {}ff1;};", "ERROR:test(1):Field can be instantiated only inside Register\n"),
    ("reg rr{field {}ff1[1:0]; field {}ff2[2:3];};", "ERROR:test(1):field bit order do not match register bit order\n"),
    ("reg rr{field {}ff1[32:0];};", "ERROR:test(1):field position out of range of register width\n"),
    ("reg rr{field {}ff1[1:0]; field {}ff2[2:1];};", "ERROR:test(1):field position overlaps with a previous field\n"),
    # enterExplicit_property_assign
    ("default posedge intr;", "ERROR:test(1):property modifier not allowed in default\n"),
    ("default name = 1;", "ERROR:test(1):name expected string value\n"),
    ("default namea = 1;", "ERROR:test(1):namea is not a builtin property\n"),
    ("default sw = 1;", "ERROR:test(1):sw expected accessType\n"),
    ("field ff {posedge we;};", "ERROR:test(1):property modifier is allowed only for\'intr\' on Field\n"),
    # enterPost_property_assign
    ("regfile rf{reg {field {}ff;}rr; rr.ff = 1;};", "ERROR:test(1):property is not specified\n"),
    # Component.py
    # Component.set_property
    ("field ff{we; wel;};", "ERROR:test(1):properties we, wel should be exclusive in Field ff\n"),
    # Component.validate_property
    ("reg rr{field {}ff; ff->fieldwidth = 32;};", "ERROR:test(1):property fieldwidth cannot be assigned dynamically\n"),
    ("field ff{sw=1;};", "ERROR:test(1):property sw expected accessType\n"),
    ("field ff{lsb0;};", "ERROR:test(1):property lsb0 not defined for Field\n"),
    ("property p_fld{component=field; type=string;}; field ff{p_fld = 1;};",
     "ERROR:test(1):property p_fld expected string\n"),
    # Component.add_comp
    ("reg rr{reg {}rr1;};", "ERROR:test(1):Register instance not allowed in Register\n"),
    ("reg rr{field {}ff; field {}ff;};", "ERROR:test(1):all instance names should be unique within a scope\n"),
    # AddrMap.validate_property
    ("addrmap am{alignment = 31;};", "ERROR:test(1):property alignment should be a power of two\n"),
    # AddrMap.validate_addresses
    ("field ff{};addrmap am{reg {ff ff1;}rr1; reg {ff ff1;}rr2@0x0;};",
     "ERROR:test(1):address 0x0 of register rr2 already assigned\n"),
    # RegFile.validate_property
    ("regfile rf{alignment = 31;};", "ERROR:test(1):property alignment should be a power of two\n"),
    # Register.validate_property
    ("reg rr{regwidth=7;};", "ERROR:test(1):property regwidth should be a power of two and >= 8\n"),
    # Field.check_type
    ("field ff{reset=1;};", "ERROR:test(1):verilog style integer should be used for non-zero reset values\n"),
    # Field.validate_property
    ("reg rr{field {fieldwidth=1;}ff1[2];};",
     "ERROR:test(1):field instantiation width does not match explicitly defined field width\n"),
    ("reg rr{field {}ff; ff->reset = ff;};", "ERROR:test(1):reset cannot be self-referencing\n"),
    ("signal{}ss[2];reg rr{field{}ff;ff->reset=ss;};",
     "ERROR:test(1):size of reset value signal does not match field width\n"),
    ("reg rr{field {}ff;ff->reset=2'h0;};", "ERROR:test(1):size of reset value does not match field width\n"),
    ("reg rr{field {reset=2'h0;}ff;};", "ERROR:test(1):size of reset value does not match field width\n"),
    ("signal{}ss[2];reg rr{field{reset=ss;}ff;};", "ERROR:test(1):size of reset value does not match field width\n"),
    ("enum ee{aa=2'd0;}; reg rr{field {encode=ee;}ff;};",
     "ERROR:test(1):enumeration values do not fit within field width\n"),
    ("signal{}ss[2];reg rr{field{resetsignal=ss;}ff;};", "ERROR:test(1):width of resetsignal signal should be 1\n"),
    ("field ff{sw=w;hw=w;};", "ERROR:test(1):invalid field access pair in Field\n"),
    ("enum ee{aa=2'd0;}; field ff{fieldwidth=1;encode=ee;};",
     "ERROR:test(1):enumeration values do not fit within field width\n"),
    # Signal.validate_property
    ("signal {signalwidth=2;}ss;",
     "ERROR:test(1):signal instantiation width does not match explicitly defined signal width\n"),
]
