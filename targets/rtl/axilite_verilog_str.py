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
clock_comment = '    // Clocks\n'
pl_port_comment = '    // PL Ports\n'
axi_ports_end = '''    // AXILite Signal
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

internal_signals = '''
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

'''

reg_signal = '  reg [{width}:0] {name};\n'

begin_io_assgns_axi_logic = '''
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
'''

axi_write_header = '''
  always @( posedge s_axi_aclk )
  begin : axi_write_proc
    reg [OPT_MEM_ADDR_BITS:0] loc_addr;
    if ( s_axi_areset == 1'b1 )
      begin'''
axi_write_reset_reg = '\n'+'  '*4+'{name}[{msb}:{lsb}] <= 0;'
axi_write_else_header = '''
      end 
    else begin
      loc_addr = axi_awaddr[ADDR_LSB+OPT_MEM_ADDR_BITS:ADDR_LSB];
      if (slv_reg_wren) begin'''
axi_write_assign = '''
        if (loc_addr == {len}'b{val}) begin
          for ( byte_index = 0; byte_index <= (C_S_AXI_DATA_WIDTH/8)-1; byte_index = byte_index+1 ) begin
            if ( s_axi_wstrb[byte_index] == 1 ) begin
              {name}[(byte_index*8) +: 8] <= s_axi_wdata[(byte_index*8) +: 8];
            end
          end'''
axi_write_assign_else = '\n        end else begin'
axi_write_assign_end = '\n        end'
axi_write_else = '\n      end else begin'
axi_sclr_part1 = '{'
axi_sclr_part2 = ', '
axi_sclr_part3 = '[{}:{}]'
axi_sclr_part4 = '{size}\'b{val}'
axi_sclr_part5 = '};'
axi_write_footer = '''
      end
    end
  end
'''
axi_logic2 = '''

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
reg_data_out_when = '''
          {size}'b{num_bin}   : reg_data_out <= {name};'''
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
