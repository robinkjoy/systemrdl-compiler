libraries = ''
entity_header = '''`timescale 1 ns / 1 ps

module axilite_reg_if #
  (
    // Width of S_AXI data bus
    parameter integer C_S_AXI_DATA_WIDTH = 32,
    // Width of S_AXI address bus
    parameter integer C_S_AXI_ADDR_WIDTH = 8
  )
  (
'''
st_in = '    input  wire {name},\n'
st_out = '    output wire {name},\n'
sv_in = '    input  wire [{width}:0] {name},\n'
sv_out = '    output wire [{width}:0] {name},\n'
field_reset = '''\
    // Field Reset
    input wire rst,
'''
pl_port_field_comment = '    // PL Field Ports\n'
pl_port_signal_comment = '    // Custom Signal Ports\n'
axi_ports_end = '''    // AXILite Signals
    input wire  s_axi_aclk,
    input wire  s_axi_areset,
    input wire [C_S_AXI_ADDR_WIDTH-1 : 0] s_axi_awaddr,
    input wire [2 : 0] s_axi_awprot,
    input wire  s_axi_awvalid,
    output wire  s_axi_awready,
    input wire [C_S_AXI_DATA_WIDTH-1 : 0] s_axi_wdata,
    input wire [(C_S_AXI_DATA_WIDTH/8)-1 : 0] s_axi_wstrb,
    input wire  s_axi_wvalid,
    output wire  s_axi_wready,
    output wire [1 : 0] s_axi_bresp,
    output wire  s_axi_bvalid,
    input wire  s_axi_bready,
    input wire [C_S_AXI_ADDR_WIDTH-1 : 0] s_axi_araddr,
    input wire [2 : 0] s_axi_arprot,
    input wire  s_axi_arvalid,
    output wire  s_axi_arready,
    output wire [C_S_AXI_DATA_WIDTH-1 : 0] s_axi_rdata,
    output wire [1 : 0] s_axi_rresp,
    output wire  s_axi_rvalid,
    input wire  s_axi_rready
    );
'''

components = ''

constants = '''
  localparam integer ADDR_LSB = (C_S_AXI_DATA_WIDTH/32) + 1;
  localparam integer OPT_MEM_ADDR_BITS = {};
'''

axi_internal_signals = '''
  // AXI4LITE signals
  reg [C_S_AXI_ADDR_WIDTH-1 : 0]   axi_awaddr;
  reg    axi_awready;
  reg    axi_wready;
  reg [1 : 0]   axi_bresp;
  reg    axi_bvalid;
  reg [C_S_AXI_ADDR_WIDTH-1 : 0]   axi_araddr;
  reg    axi_arready;
  reg [C_S_AXI_DATA_WIDTH-1 : 0]   axi_rdata;
  reg [1 : 0]   axi_rresp;
  reg    axi_rvalid;

  wire   slv_reg_rden;
  wire   slv_reg_wren;
  reg [C_S_AXI_DATA_WIDTH-1:0]   reg_data_out;
  integer   byte_index;
  
  // Registers
'''

reg_signal = '  reg [{width}:0] {name};\n'
reg_signal_1bit = '  reg {name};\n'

write_addr_decode_comment = '\n  // Write Address Decode Signals\n'
internal_signals_comment = '\n  // Internal Signals\n'

begin = '''
'''

signal_explicit_header = '''
  // Explicit signals
'''

signal_implicit_header = '''
  // Implicit signals
'''

signal_assign_prop = '  assign {name} = {op}{reg}[{msb}:{lsb}];'
signal_assign = '  assign {name} = {reg}[{msb}:{lsb}];'

write_addr_decode_header = '''

  // Write Address Decoder
  always@(axi_awaddr or slv_reg_wren) begin
'''

write_addr_decode_default = '''\
    {name}_axi_we <= 1b'0;
'''

write_addr_decode_case = '''\
    case(axi_awaddr)
'''

write_addr_decode = '''\
      {bits}'b{addr:0{bits}b} : {name}_axi_we <= slv_reg_wren;
'''

write_addr_decode_footer = '''\
    endcase
  end
'''

write_comment = '''
  // Field writes
'''

bin_num = '{bits}\'b{value:0{bits}b}'

axi_write_reset_sync = '''\
  // {field_name}
  always@(posedge clk) begin
    if ({rst} == 1'b{active}) begin
      {reg_name}[{msb}:{lsb}] <= {value};
    end else begin
      '''

axi_write_reset_async = '''\
  // {field_name}
  always@(posedge clk or {active_edge}edge {rst}) begin
    if ({rst} == 1'b{active}) begin
      {reg_name}[{msb}:{lsb}] <= {value};
    end else begin
      '''

axi_write_field_else = ' else '

axi_write_field_hw_we = '''\
if ({ctrl} == 1'b{active}) begin
        {reg}[{msb}:{lsb}] <= {field};
      end'''

axi_write_field_hw_we_mask = '''\
if ({ctrl} == 1'b{active}) begin
        for (i=0; i<{size}; i=i+1) begin
          if ({mask}[i] == 1'b{mask_active}) begin
            {reg}[{lsb}+i] <= {field};
          end
        end
      end'''

axi_write_field_hw_set = '''\
if ({ctrl} == 1'b{active}) begin
        {reg}[{msb}:{lsb}] <= {size}'b{field};
      end'''

axi_write_field_hw_set_mask = '''\
if ({ctrl} == 1'b{active}) begin
        for (i=0; i<{size}; i=i+1) begin
          if ({mask}[i] == 1'b{mask_active}) begin
            {reg}[{lsb}+i] <= 1'b{field};
          end
        end
      end'''

axi_write_field_sw = '''if ({reg}_axi_we == 1'b1) begin
        {reg}[{msb}:{lsb}] <= s_axi_wdata[{msb}:{lsb}];
      end'''

axi_write_field_hw_pre = '''      begin
  '''
axi_write_field_hw = '      {reg}[{msb}:{lsb}] <= {value};'
axi_write_field_hw_post = '      end'

axi_write_field_hw_clr = '''begin
        {reg}[{msb}:{lsb}] <= {size}'b{value};
      end'''

axi_write_field_footer = '''
      end
    end
  end

'''

axi_logic2 = '''

  // I/O Connections assignments
  assign s_axi_awready  = axi_awready;
  assign s_axi_wready  = axi_wready;
  assign s_axi_bresp  = axi_bresp;
  assign s_axi_bvalid  = axi_bvalid;
  assign s_axi_arready  = axi_arready;
  assign s_axi_rdata  = axi_rdata;
  assign s_axi_rresp  = axi_rresp;
  assign s_axi_rvalid  = axi_rvalid;

  always @( posedge s_axi_aclk )
  begin
    if ( s_axi_areset == 1'b1 )
      begin
        axi_awready <= 1'b0;
      end 
    else
      begin    
        if (~axi_awready && s_axi_awvalid && s_axi_wvalid)
          begin
            axi_awready <= 1'b1;
          end
        else           
          begin
            axi_awready <= 1'b0;
          end
      end 
  end       

  always @( posedge s_axi_aclk )
  begin
    if ( s_axi_areset == 1'b1 )
      begin
        axi_awaddr <= 0;
      end 
    else
      begin    
        if (~axi_awready && s_axi_awvalid && s_axi_wvalid)
          begin
            axi_awaddr <= s_axi_awaddr;
          end
      end 
  end       

  always @( posedge s_axi_aclk )
  begin
    if ( s_axi_areset == 1'b1 )
      begin
        axi_wready <= 1'b0;
      end 
    else
      begin    
        if (~axi_wready && s_axi_wvalid && s_axi_awvalid)
          begin
            axi_wready <= 1'b1;
          end
        else
          begin
            axi_wready <= 1'b0;
          end
      end 
  end       

  assign slv_reg_wren = axi_wready && s_axi_wvalid && axi_awready && s_axi_awvalid;
  // Write Response
  always @( posedge s_axi_aclk )
  begin
    if ( s_axi_areset == 1'b1 )
      begin
        axi_bvalid  <= 0;
        axi_bresp   <= 2'b0;
      end 
    else
      begin    
        if (axi_awready && s_axi_awvalid && ~axi_bvalid && axi_wready && s_axi_wvalid)
          begin
            axi_bvalid <= 1'b1;
            axi_bresp  <= 2'b0;
          end
        else
          begin
            if (s_axi_bready && axi_bvalid) 
              begin
                axi_bvalid <= 1'b0; 
              end  
          end
      end
  end   

  always @( posedge s_axi_aclk )
  begin
    if ( s_axi_areset == 1'b1 )
      begin
        axi_arready <= 1'b0;
        axi_araddr  <= 32'b0;
      end 
    else
      begin    
        if (~axi_arready && s_axi_arvalid)
          begin
            axi_arready <= 1'b1;
            axi_araddr  <= s_axi_araddr;
          end
        else
          begin
            axi_arready <= 1'b0;
          end
      end 
  end       

  always @( posedge s_axi_aclk )
  begin
    if ( s_axi_areset == 1'b1 )
      begin
        axi_rvalid <= 0;
        axi_rresp  <= 0;
      end 
    else
      begin    
        if (axi_arready && s_axi_arvalid && ~axi_rvalid)
          begin
            axi_rvalid <= 1'b1;
            axi_rresp  <= 2'b0; // 'OKAY' response
          end   
        else if (axi_rvalid && s_axi_rready)
          begin
            axi_rvalid <= 1'b0;
          end                
      end
  end    

  assign slv_reg_rden = axi_arready & s_axi_arvalid & ~axi_rvalid;
'''

reg_data_out_header = '''
  always @(*)
  begin
    if ( s_axi_areset == 1'b1 )
      begin
        reg_data_out <= 0;
      end 
    else
      begin    
        case ( axi_araddr[ADDR_LSB+OPT_MEM_ADDR_BITS:ADDR_LSB] )'''

concat_pre = '{'
concat = ', '
bit_select = '[{msb}:{lsb}]'
concat_post = '}'

reg_data_out_when = '''
          {size}'b{num_bin}   : reg_data_out <= {value};'''

reg_data_out_footer_axi_logic = '''
          default : reg_data_out <= 0;
        endcase
      end   
  end

  always @( posedge s_axi_aclk )
  begin
    if ( s_axi_areset == 1'b1 )
      begin
        axi_rdata  <= 0;
      end 
    else
      begin    
        if (slv_reg_rden)
          begin
            axi_rdata <= reg_data_out;
          end   
      end
  end
'''

ctrl_sig_assgns_header = '\n  // Assign registers to control signals\n'
ctrl_sig_assgns = '  assign {} = s{}[{}:{}];\n'
ctrl_sig_assgns_1bit = '  assign {} = {}[{}];\n'

sts_sig_assgns_header = '''
  // Assign status signals to registers
  always@(posedge s_axi_aclk)
  begin : stat_to_reg_proc
    reg [OPT_MEM_ADDR_BITS:0] loc_addr;
    if (s_axi_areset == 1'b1) begin'''

sts_sig_assgns_reset = '\n      {} <= 0;'
sts_sig_assgns_reset_else = '''
    end else begin
      loc_addr = axi_awaddr[ADDR_LSB + OPT_MEM_ADDR_BITS:ADDR_LSB];'''
sts_sig_assgns_no_clr = '\n      {reg_name}[{msb}:{lsb}] <= {signal};'
sts_sig_assgns_no_clr_1bit = '\n      {reg_name}[{msb}] <= {signal};'
sts_sig_assgns_with_clr = '''
      if ({signal_valid} == 1'b1) begin
        {reg_name}({msb} downto {lsb}) <= {signal};
      end else if (slv_reg_wren == 1'b1 && loc_addr == {size}'b{addr_bin}
        && s_axi_wstrb[{strb_lsb}:{strb_msb}] == "{strb_1s}" then
        {reg_name}({msb} downto {lsb}) <= (others => \'0\');
      else
        {reg_name}({msb} downto {lsb}) <= {reg_name}({msb} downto {lsb});
      end'''
sts_sig_assgns_with_clr_1bit = '''
      if ({signal_valid} == 1'b1) begin
        {reg_name}[{msb}] <= {signal};
      end else if (slv_reg_wren == 1'b1 && loc_addr == {size}'b{addr_bin}
        && s_axi_wstrb[{strb_lsb}:{strb_msb}] == {strb_size}'b{strb_1s}) begin
        {reg_name}[{msb}] <= 1\'b0;
      end else begin
        {reg_name}[{msb}] <= {reg_name}[{msb}];
      end'''
sts_sig_assgns_footer = '''
    end
  end
'''
arc_footer = '\nendmodule'
