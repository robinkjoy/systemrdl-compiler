from math import log2, ceil
import logging

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
            if field.hw == 'na':
                continue
            port_name = field.get_full_name()
            if 'w' in field.hw:
                port_str = rtl_str.st_in if field.fieldwidth == 1 else rtl_str.sv_in
                f.write(port_str.format(name=port_name+'_i',
                                             width=field.fieldwidth))
            if 'r' in field.hw:
                port_str = rtl_str.st_out if field.fieldwidth == 1 else rtl_str.sv_out
                f.write(port_str.format(name=port_name+'_o',
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
    for i, reg in enumerate(regs):
        f.write(rtl_str.reg_signal.format(name=reg.get_full_name(),
                                          width=reg.regwidth - 1))


def write_reg_resets(f, regs):
    for i, reg in enumerate(regs):
        for field in reg.comps:
            if 'r' in field.hw:
                f.write(rtl_str.axi_write_reset_reg.format(
                    name=reg.get_full_name(),
                    msb=field.position[0], lsb=field.position[1]))


def write_axi_keep_value(i, reg, indent):
    slv = 'slv_reg' + str(i)
    sclr = []
    s = ''
    for field in reg.comps:
        if field.singlepulse:
            sclr.append(field)
    if sclr:
        s = '\n' + ' ' * indent + slv + ' <= '
        sclr.sort(key=lambda x: x.position[0], reverse=True)
        prev_lsb = reg.regwidth - 1
        s += rtl_str.axi_sclr_part1
        for j, field in enumerate(sclr):
            if j != 0:
                s += rtl_str.axi_sclr_part2
            msb, lsb = max(field.position), min(field.position)
            if prev_lsb != msb:
                s += slv + rtl_str.axi_sclr_part3.format(prev_lsb, lsb + 1)
                s += rtl_str.axi_sclr_part2
            prev_lsb = lsb - 1
            zeros = msb - lsb + 1
            s += rtl_str.axi_sclr_part4.format(size=zeros, val='0' * zeros)
        if prev_lsb != -1:
            s += rtl_str.axi_sclr_part2
            s += slv + rtl_str.axi_sclr_part3.format(prev_lsb, 0)
        s += rtl_str.axi_sclr_part5
    return s


def write_axi_writes(f, regs, mem_addr_bits, lang):
    indent = 14 if lang == 'vhdl' else 10
    for i, reg in enumerate(regs):
        # if reg.placcess == 'r':
        f.write(rtl_str.axi_write_assign.format(len=mem_addr_bits,
                                                val=format(reg.addr // 4, '0' + str(mem_addr_bits) + 'b'),
                                                name=reg.get_full_name()))  # fixme addr accesswidth
        s = write_axi_keep_value(i, reg, indent)
        if s != '':
            f.write(rtl_str.axi_write_assign_else)
            f.write(s)
        f.write(rtl_str.axi_write_assign_end)


def write_axi_keep_values(f, regs, lang):
    s = ''
    indent = 12 if lang == 'vhdl' else 8
    for i, reg in enumerate(regs):
        s += write_axi_keep_value(i, reg, indent)
    if s != '':
        f.write(rtl_str.axi_write_else)
        f.write(s)


def reg_data_out_sensitivity(regs):
    s = ''
    for i in range(len(regs)):
        s += 'slv_reg' + str(i) + ', '
    return s


def write_reg_data_out_when(f, regs, mem_addr_bits):
    for i, reg in enumerate(regs):
        f.write(rtl_str.reg_data_out_when.format(size=mem_addr_bits,
                                                 num_bin=format(reg.addr // 4, '0' + str(mem_addr_bits) + 'b'),
                                                 name=reg.get_full_name()))  # fixme addr accesswidth


def write_ctrl_sig_assgns(f, regs):
    for i, reg in enumerate(regs):
        for field in reg.comps:
            sig_name = field.get_full_name()
            if field.position[0] == field.position[1]:
                f.write(rtl_str.ctrl_sig_assgns_1bit.format(
                    sig_name, reg.get_full_name(), field.position[0]))
            else:
                f.write(rtl_str.ctrl_sig_assgns.format(
                    sig_name, reg.get_full_name(), field.position[0], field.position[1]))


def write_sts_sig_resets(f, regs):
    for i, reg in enumerate(regs):
        f.write(rtl_str.sts_sig_assgns_reset.format(reg.get_full_name()))


def write_sts_sig_assgns(f, regs):
    for i, reg in enumerate(regs):
        for field in reg.comps:
            if 'w' in field.hw:
                continue
            sig_name = reg.name.lower() + '_' + field.name.lower()
            # if field.access == 'rwclr':
            #     if field.msb == field.lsb:
            #        tmpl = rtl_str.sts_sig_assgns_with_clr_1bit
            #     else:
            #        tmpl = rtl_str.sts_sig_assgns_with_clr
            #     f.write(tmpl.format(
            #         signal_valid=sig_name+'_vld',
            #         reg_name=reg.get_full_name(), msb=field.msb, lsb=field.lsb,
            #         signal=sig_name,
            #         addr_bin=format(i, '0'+str(mem_addr_bits)+'b'),
            #         size=mem_addr_bits,
            #         strb_msb=field.msb//8, strb_lsb=field.lsb//8,
            #         strb_1s='1'*(field.msb//8-field.lsb//8+1),
            #         strb_size=field.msb//8-field.lsb//8+1
            #         ))
            # else:
            #     tmpl = rtl_str.sts_sig_assgns_no_clr_1bit if field.msb == field.lsb else rtl_str.sts_sig_assgns_no_clr
            #     f.write(tmpl.format(reg_name=reg.get_full_name(), msb=field.position[0],
            # lsb=field.position[1], signal=sig_name))
            tmpl = rtl_str.sts_sig_assgns_no_clr_1bit if field.position[0] == field.position[
                1] else rtl_str.sts_sig_assgns_no_clr
            f.write(tmpl.format(reg_name=reg.get_full_name(), msb=field.position[0], lsb=field.position[1],
                                signal=sig_name))


# main function
def generate_rtl(lang, addrmap, last_addr, root_sigs, internal_sigs):
    import_strings(lang)
    regs = list(addrmap.get_regs_iter())
    file_ext = 'v' if lang == 'verilog' else 'vhd'
    filename = 'outputs/{}.{}'.format(addrmap.def_id, file_ext)
    f = open(filename, 'w')
    f.write(rtl_str.libraries)
    f.write(rtl_str.entity_header.format(32, 8))
    signals = root_sigs+list(addrmap.get_sigs_iter())
    write_ports_fields(f, regs)
    write_ports_signals(f, signals)
    f.write(rtl_str.axi_ports_end)
    mem_addr_bits = ceil(log2(max(last_addr, 31))) - 2  # axi width = 32, access = 32 fixme
    f.write(rtl_str.constants.format(mem_addr_bits - 1))
    f.write(rtl_str.axi_internal_signals)
    write_reg_signals(f, regs)
    f.write('\n')
    f.write(rtl_str.begin_io_assgns_axi_logic)
    f.write(rtl_str.axi_write_header)
    write_reg_resets(f, regs)
    f.write(rtl_str.axi_write_else_header)
    write_axi_writes(f, regs, mem_addr_bits, lang)
    write_axi_keep_values(f, regs, lang)
    f.write(rtl_str.axi_write_footer)
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
