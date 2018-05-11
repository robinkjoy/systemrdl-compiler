test_strings = [
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
    # extract_enum_body
    ("enum ee{};", "ERROR:test(1):no entries in enum\n"),
    ("enum ee{aa=1;};", "ERROR:test(1):enum entry value should be sizedNumeric\n"),
    ("enum ee{aa=1'b0;aa=1'b1;};", "ERROR:test(1):aa already defined in enum\n"),
    ("enum ee{aa=2'h0;ab=1'b1;};", "ERROR:test(1):size does not match others\n"),
    ("enum ee{aa=1'h0;ab=1'b0;};", "ERROR:test(1):1'b0 already defined in enum\n"),
    # extract_instance_ref
    ('''\
     addrmap am {
        reg {
            field {} ff;
        } rr[2];
        rr.ff->sw = r;
     };
     ''', "ERROR:test(5):array index for rr not specified\n"),
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
]
