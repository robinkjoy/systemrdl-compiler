from math import log2, ceil
import logging

from Component import Component

log = logging.getLogger()


def import_strings(lang):
    global rtl_str
    if lang == 'verilog':
        import targets.rtl.axilite_verilog_str as rtl_str
    else:
        import targets.rtl.axilite_vhdl_str as rtl_str


def write_ports_fields(f, regs):
    f.write(rtl_str.pl_port_field_comment)
    for reg in regs:
        for field in reg.comps:
            if field.hw == 'na' or field.next is not None:
                continue
            port_name = field.get_full_name()
            if 'w' in field.hw:
                port_str = rtl_str.st_in if field.fieldwidth == 1 else rtl_str.sv_in
                f.write(port_str.format(name=port_name + '_i',
                                        width=field.fieldwidth))
            if 'r' in field.hw:
                port_str = rtl_str.st_out if field.fieldwidth == 1 else rtl_str.sv_out
                f.write(port_str.format(name=port_name + '_o',
                                        width=field.fieldwidth))


def write_ports_signals(f, signals):
    f.write(rtl_str.pl_port_signal_comment)
    for sig in signals:
        if not sig.input and not sig.output:
            log.warning(f'signal {sig.inst_id} is unused. skipping', sig.line)
        if sig.input and not sig.output:
            port_str = rtl_str.st_in if sig.signalwidth == 1 else rtl_str.sv_in
            f.write(port_str.format(name=sig.get_full_name(), width=sig.signalwidth))
        if not sig.input and sig.output:
            port_str = rtl_str.st_out if sig.signalwidth == 1 else rtl_str.sv_out
            f.write(port_str.format(name=sig.get_full_name(), width=sig.signalwidth))


def write_reg_signals(f, regs):
    for reg in regs:
        f.write(rtl_str.reg_signal.format(name=reg.get_full_name(),
                                          width=reg.regwidth - 1))


def write_write_addr_decode_signals(f, regs):
    f.write(rtl_str.write_addr_decode_comment)
    for reg in regs:
        if any(field for field in reg.comps if 'w' in field.sw):
            f.write(rtl_str.reg_signal_1bit.format(name=reg.get_full_name() + '_axi_we'))


def write_internal_signals(f, internal_signals):
    for sig in internal_signals:
        sig_str = rtl_str.reg_signal_1bit if sig.signalwidth == 1 else rtl_str.reg_signal
        name = sig.int_ref[0].get_full_name()
        if sig.int_ref[1] is not None:
            name += '_'+sig.int_ref[1]
        f.write(sig_str.format(name=name, width=sig.signalwidth))


def write_signal_assignments(f, regs, internal_sigs):
    f.write(rtl_str.signal_explicit_header)
    op_str_dict = {'anded': '&', 'ored': '|', 'xored': '^'}
    for reg in regs:
        for field in reg.comps:
            for prop in ['anded', 'ored', 'xored']:
                value = getattr(field, prop, False)
                if not value:
                    continue
                name=field.get_full_name()+'_'+prop if value is True else value.get_full_name()
                f.write(rtl_str.signal_assign_prop.format(name=name, op_str=prop, op=op_str_dict[prop],
                                                          reg=reg.get_full_name(),
                                                          msb=field.position[0], lsb=field.position[1]))
    f.write(rtl_str.signal_implicit_header)
    for sig in internal_sigs:
        if not sig.output:
            continue
        ifield = sig.int_ref[0]
        iprop = sig.int_ref[1]
        if iprop is None:
            f.write(rtl_str.signal_assign.format(name=ifield.get_full_name(), reg=ifield.parent.get_full_name(),
                                                 msb=ifield.position[0], lsb=ifield.position[1]))
        else:
            rtl_str.signal_assign_prop.format(name=ifield.get_full_name()+'_'+iprop, op_str=iprop,
                                              op=op_str_dict[iprop], reg=ifield.parent.get_full_name(),
                                              msb=ifield.position[0], lsb=ifield.position[1])


def write_write_addr_decode(f, regs, mem_addr_bits):
    f.write(rtl_str.write_addr_decode_header)
    for reg in regs:
        if any(field for field in reg.comps if 'w' in field.sw):
            f.write(rtl_str.write_addr_decode_default.format(
                name=reg.get_full_name() + '_axi_we'))
    f.write(rtl_str.write_addr_decode_case)
    for reg in regs:
        if any(field for field in reg.comps if 'w' in field.sw):
            f.write(rtl_str.write_addr_decode.format(
                name=reg.get_full_name() + '_axi_we',
                addr=reg.addr, bits=mem_addr_bits))
    f.write(rtl_str.write_addr_decode_footer)


def write_axi_write_reset(f, reg, field):
    if getattr(field, 'resetsignal', None) is not None:
        rst = field.resetsignal.get_full_name()
        active_high = getattr(field.resetsignal, 'activehigh', False) \
                      or not getattr(field.resetsignal, 'activelow', False)
        sync = getattr(field.resetsignal, 'sync', False) \
               or not getattr(field.resetsignal, 'async', False)
    else:
        rst = 'rst'
        active_high = True
        sync = True
    axi_write_reset_str = rtl_str.axi_write_reset_sync if sync else rtl_str.axi_write_reset_async
    value = getattr(field, 'reset', None)
    if value is not None:
        if isinstance(value, Component):
            value = value.get_full_name()
        else:
            value = rtl_str.bin_num.format(bits=field.fieldwidth, value=value)
    else:
        value = rtl_str.bin_num.format(bits=field.fieldwidth, value=0)
    f.write(axi_write_reset_str.format(field_name=field.get_full_name(),
                                       active_edge='pos' if active_high else 'neg', rst=rst,
                                       active=1 if active_high else 0, reg_name=reg.get_full_name(),
                                       msb=field.position[0], lsb=field.position[1], value=value))


def get_hw_mask(field):
    if field.hwenable:
        return field.hwenable.get_full_name(), 1
    elif field.hwmask:
        return field.hwmask.get_full_name(), 0
    else:
        return None, None


def write_field_hw_access_we(f, reg, field, skipped):
    we = getattr(field, 'we', None)
    wel = getattr(field, 'wel', None)
    if not we and not wel:
        return skipped
    if not skipped:
        f.write(rtl_str.axi_write_field_else)
    # if true or signal
    if we:
        active = '1'
        attr = we
        attr_str = 'we'
    else:
        active = '0'
        attr = wel
        attr_str = 'wel'
    if attr is True:
        ctrl = field.get_full_name() + '_' + attr_str
    else:
        ctrl = attr.get_full_name()
    mask, mask_active = get_hw_mask(field)
    hw_str = rtl_str.axi_write_field_hw_we_mask if mask else rtl_str.axi_write_field_hw_we
    size = field.fieldwidth
    f.write(hw_str.format(ctrl=ctrl, active=active, reg=reg.get_full_name(),
                          msb=field.position[0], lsb=field.position[1],
                          field=field.get_full_name(), size=size,
                          mask=mask, mask_active=mask_active))
    return False


def write_field_hw_access_hwsetclr(f, reg, field, skipped):
    hwset = getattr(field, 'hwset', None)
    hwclr = getattr(field, 'hwclr', None)
    if not hwset and not hwclr:
        return skipped
    if not skipped:
        f.write(rtl_str.axi_write_field_else)
    if hwset:
        attr = hwset
        attr_str = 'hwset'
        field_str = '1'
    else:
        attr = hwclr
        attr_str = 'hwclr'
        field_str = '0'
    if attr is True:
        ctrl = field.get_full_name() + '_' + attr_str
        active = '1'
    else:
        ctrl = attr.get_full_name()
        if getattr(attr, 'activehigh', False) or not getattr(attr, 'activelow', False):
            active = '1'
        else:
            active = '0'
    mask, mask_active = get_hw_mask(field)
    hw_str = rtl_str.axi_write_field_hw_set_mask if mask else rtl_str.axi_write_field_hw_set
    size = field.fieldwidth
    field_str = size * field_str if mask else field_str
    f.write(hw_str.format(ctrl=ctrl, active=active, reg=reg.get_full_name(),
                          msb=field.position[0], lsb=field.position[1],
                          field=field_str, size=size,
                          mask=mask, mask_active=mask_active))
    return False


def write_field_sw_access(f, reg, field, skipped):
    if 'w' not in field.sw:
        return skipped
    if not skipped:
        f.write(rtl_str.axi_write_field_else)
    f.write(rtl_str.axi_write_field_sw.format(reg=reg.get_full_name(), msb=field.position[0], lsb=field.position[1]))
    return False


def write_field_hw_access(f, reg, field, skipped):
    if 'w' not in field.sw or field.we or field.wel:
        return skipped
    if not skipped:
        f.write(rtl_str.axi_write_field_hw_pre)
    value = field.next.get_full_name() if field.next else field.get_full_name()+'_i'
    f.write(rtl_str.axi_write_field_hw.format(reg=reg.get_full_name(), msb=field.position[0],
                                              lsb=field.position[1], value=value))
    if not skipped:
        f.write(rtl_str.axi_write_field_hw_post)
    return False


def write_field_singlepulse(f, reg, field, skipped):
    if not field.singlepulse:
        return skipped
    f.write(rtl_str.axi_write_field_hw_clr.format(reg=reg.get_full_name(), msb=field.position[0], lsb=field.position[1],
                                                  size=field.fieldwidth, value='0' * field.fieldwidth))
    return False


def write_axi_writes(f, regs):
    f.write(rtl_str.write_comment)
    for reg in regs:
        for field in reg.comps:
            if 'w' not in field.sw and 'rw' != field.hw:
                continue
            write_axi_write_reset(f, reg, field)
            skipped = write_field_hw_access_we(f, reg, field, True)
            skipped = write_field_hw_access_hwsetclr(f, reg, field, skipped)
            skipped = write_field_sw_access(f, reg, field, skipped)
            skipped = write_field_hw_access(f, reg, field, skipped)
            skipped = write_field_singlepulse(f, reg, field, skipped)
            f.write(rtl_str.axi_write_field_footer)


def reg_data_out_sensitivity(regs):
    s = ''
    for i in range(len(regs)):
        s += 'slv_reg' + str(i) + ', '
    return s


def field_concat(reg, fields):
    concat = rtl_str.concat_pre
    first = True
    last_lsb = reg.regwidth
    for field in fields:
        if last_lsb != field.position[0]+1:
            if not first:
                concat += rtl_str.concat
            first = False
            concat += rtl_str.bin_num.format(bits=last_lsb-field.position[0]-1, value=0)
        if not first:
            concat += rtl_str.concat
        first = False
        concat += reg.get_full_name()
        concat += rtl_str.bit_select.format(msb=field.position[0], lsb=field.position[1])
        last_lsb = field.position[1]
    if last_lsb != 0:
        if not first:
            concat += rtl_str.concat
        concat += rtl_str.bin_num.format(bits=last_lsb, value=0)
    concat += rtl_str.concat_post
    return concat


def write_reg_data_out_when(f, regs, mem_addr_bits):
    # fixme addr accesswidth
    for reg in regs:
        sw_r_fields = [f for f in reg.comps if 'r' in f.sw]
        sw_r_fields.sort(key=lambda x: x.position[0], reverse=True)
        f.write(rtl_str.reg_data_out_when.format(size=mem_addr_bits,
                                                 num_bin=format(reg.addr // 4, '0' + str(mem_addr_bits) + 'b'),
                                                 value=field_concat(reg, sw_r_fields)))


def write_ctrl_sig_assgns(f, regs):
    for reg in regs:
        for field in reg.comps:
            sig_name = field.get_full_name()
            if field.position[0] == field.position[1]:
                f.write(rtl_str.ctrl_sig_assgns_1bit.format(
                    sig_name, reg.get_full_name(), field.position[0]))
            else:
                f.write(rtl_str.ctrl_sig_assgns.format(
                    sig_name, reg.get_full_name(), field.position[0], field.position[1]))


def write_sts_sig_resets(f, regs):
    for reg in regs:
        f.write(rtl_str.sts_sig_assgns_reset.format(reg.get_full_name()))


def write_sts_sig_assgns(f, regs):
    for reg in regs:
        for field in reg.comps:
            if 'w' in field.hw:
                continue
            sig_name = reg.name.lower() + '_' + field.name.lower()
            tmpl = rtl_str.sts_sig_assgns_no_clr_1bit if field.position[0] == field.position[
                1] else rtl_str.sts_sig_assgns_no_clr
            f.write(tmpl.format(reg_name=reg.get_full_name(), msb=field.position[0], lsb=field.position[1],
                                signal=sig_name))


# main function
def generate_rtl(lang, addrmap, root_sigs, internal_sigs):
    import_strings(lang)
    regs = list(addrmap.get_regs_iter())
    file_ext = 'v' if lang == 'verilog' else 'vhd'
    filename = 'outputs/{}.{}'.format(addrmap.def_id, file_ext)
    f = open(filename, 'w')
    f.write(rtl_str.libraries)
    f.write(rtl_str.entity_header.format(32, 8))
    signals = root_sigs + list(addrmap.get_sigs_iter())
    f.write(rtl_str.field_reset)
    write_ports_fields(f, regs)
    write_ports_signals(f, signals)
    f.write(rtl_str.axi_ports_end)
    mem_addr_bits = ceil(log2(max(addrmap.last_addr, 31))) - 2  # axi width = 32, access = 32 fixme
    f.write(rtl_str.constants.format(mem_addr_bits - 1))
    f.write(rtl_str.axi_internal_signals)
    write_reg_signals(f, regs)
    write_write_addr_decode_signals(f, regs)
    f.write(rtl_str.internal_signals_comment)
    write_internal_signals(f, internal_sigs)
    f.write(rtl_str.begin)
    write_signal_assignments(f, regs, internal_sigs)
    write_write_addr_decode(f, regs, mem_addr_bits)
    write_axi_writes(f, regs)
    f.write(rtl_str.axi_logic2)
    f.write(rtl_str.reg_data_out_header.format(sens=reg_data_out_sensitivity(regs)))
    write_reg_data_out_when(f, regs, mem_addr_bits)
    f.write(rtl_str.reg_data_out_footer_axi_logic)
    f.write(rtl_str.ctrl_sig_assgns_header)
    write_ctrl_sig_assgns(f, regs)
    f.write(rtl_str.sts_sig_assgns_header)
    write_sts_sig_resets(f, regs)
    f.write(rtl_str.sts_sig_assgns_reset_else)
    write_sts_sig_assgns(f, regs)
    f.write(rtl_str.sts_sig_assgns_footer)
    f.write(rtl_str.arc_footer)
    f.close()
