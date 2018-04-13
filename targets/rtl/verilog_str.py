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
  // Implement axi_awready generation
  // axi_awready is asserted for one s_axi_aclk clock cycle when both
  // s_axi_awvalid and s_axi_wvalid are asserted. axi_awready is
  // de-asserted when reset is low.

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
            // slave is ready to accept write address when 
            // there is a valid write address and write data
            // on the write address and data bus. This design 
            // expects no outstanding transactions. 
            axi_awready <= 1'b1;
          end
        else           
          begin
            axi_awready <= 1'b0;
          end
      end 
  end       

  // Implement axi_awaddr latching
  // This process is used to latch the address when both 
  // s_axi_awvalid and s_axi_wvalid are valid. 

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
            // Write Address latching 
            axi_awaddr <= s_axi_awaddr;
          end
      end 
  end       

  // Implement axi_wready generation
  // axi_wready is asserted for one s_axi_aclk clock cycle when both
  // s_axi_awvalid and s_axi_wvalid are asserted. axi_wready is 
  // de-asserted when reset is low. 

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
            // slave is ready to accept write data when 
            // there is a valid write address and write data
            // on the write address and data bus. This design 
            // expects no outstanding transactions. 
            axi_wready <= 1'b1;
          end
        else
          begin
            axi_wready <= 1'b0;
          end
      end 
  end       

  // Implement memory mapped register select and write logic generation
  // The write data is accepted and written to memory mapped registers when
  // axi_awready, s_axi_wvalid, axi_wready and s_axi_wvalid are asserted. Write strobes are used to
  // select byte enables of slave registers while writing.
  // These registers are cleared when reset (active low) is applied.
  // Slave register write enable is asserted when valid address and data are available
  // and the slave is ready to accept the write address and write data.
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
  // Implement write response logic generation
  // The write response and response valid signals are asserted by the slave 
  // when axi_wready, s_axi_wvalid, axi_wready and s_axi_wvalid are asserted.  
  // This marks the acceptance of address and indicates the status of 
  // write transaction.

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
            // indicates a valid write response is available
            axi_bvalid <= 1'b1;
            axi_bresp  <= 2'b0; // 'OKAY' response 
          end                   // work error responses in future
        else
          begin
            if (s_axi_bready && axi_bvalid) 
              //check if bready is asserted while bvalid is high) 
              //(there is a possibility that bready is always asserted high)   
              begin
                axi_bvalid <= 1'b0; 
              end  
          end
      end
  end   

  // Implement axi_arready generation
  // axi_arready is asserted for one s_axi_aclk clock cycle when
  // s_axi_arvalid is asserted. axi_awready is 
  // de-asserted when reset (active low) is asserted. 
  // The read address is also latched when s_axi_arvalid is 
  // asserted. axi_araddr is reset to zero on reset assertion.

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
            // indicates that the slave has acceped the valid read address
            axi_arready <= 1'b1;
            // Read address latching
            axi_araddr  <= s_axi_araddr;
          end
        else
          begin
            axi_arready <= 1'b0;
          end
      end 
  end       

  // Implement axi_arvalid generation
  // axi_rvalid is asserted for one s_axi_aclk clock cycle when both 
  // s_axi_arvalid and axi_arready are asserted. The slave registers 
  // data are available on the axi_rdata bus at this instance. The 
  // assertion of axi_rvalid marks the validity of read data on the 
  // bus and axi_rresp indicates the status of read transaction.axi_rvalid 
  // is deasserted on reset (active low). axi_rresp and axi_rdata are 
  // cleared to zero on reset (active low).  
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
            // Valid read data is available at the read data bus
            axi_rvalid <= 1'b1;
            axi_rresp  <= 2'b0; // 'OKAY' response
          end   
        else if (axi_rvalid && s_axi_rready)
          begin
            // Read data is accepted by the master
            axi_rvalid <= 1'b0;
          end                
      end
  end    

  // Implement memory mapped register select and read logic generation
  // Slave register read enable is asserted when valid address is available
  // and the slave is ready to accept the read address.
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
        // Address decoding for reading registers
        case ( axi_araddr[ADDR_LSB+OPT_MEM_ADDR_BITS:ADDR_LSB] )'''
reg_data_out_when = '''
          {size}'b{num_bin}   : reg_data_out <= {name};'''
reg_data_out_footer_axi_logic = '''
          default : reg_data_out <= 0;
        endcase
      end   
  end

  // Output register or memory read data
  always @( posedge s_axi_aclk )
  begin
    if ( s_axi_areset == 1'b1 )
      begin
        axi_rdata  <= 0;
      end 
    else
      begin    
        // When there is a valid read address (s_axi_arvalid) with 
        // acceptance of read address by the slave (axi_arready), 
        // output the read dada 
        if (slv_reg_rden)
          begin
            axi_rdata <= reg_data_out;     // register read data
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
cdc_inst_pl_read = '''
  cdc_sync # (
      .WIDTH      ({width}),
      .WITH_VLD   (0),
      .DAT_IS_REG (1)
      ) {signal}_cdc (
      .src_clk (s_axi_aclk),
      .src_dat ({signal}_sync),
      .src_vld (1'b1),
      .dst_clk ({clock}),
      .dst_dat ({signal}),
      .dst_vld ()
      );
'''
cdc_inst_pl_read_pulse = '''
  cdc_sync # (
      .WIDTH      ({width}),
      .WITH_VLD   (0),
      .SRC_PER_NS ({src_per}),
      .DST_PER_NS ({dst_per}),
      .IS_PULSE   (1)
      ) {signal}_cdc (
      .src_clk (s_axi_aclk),
      .src_dat ({signal}_sync),
      .src_vld (1'b1),
      .dst_clk ({clock}),
      .dst_dat ({signal}),
      .dst_vld ()
      );
'''
cdc_inst_pl_write = '''
  cdc_sync # (
      .WIDTH      ({width}),
      .WITH_VLD   (0),
      .DAT_IS_REG (0)
      ) {signal}_cdc (
      .src_clk ({clock}),
      .src_dat ({signal}),
      .src_vld (1'b1),
      .dst_clk (s_axi_aclk),
      .dst_dat ({signal}_sync),
      .dst_vld ()
      );
'''
cdc_inst_pl_write_vld = '''
  cdc_sync # (
      .WIDTH      ({width}),
      .WITH_VLD   (1),
      .SRC_PER_NS ({src_per}),
      .DST_PER_NS ({dst_per}),
      .DAT_IS_REG (0)
      ) {signal}_cdc (
      .src_clk ({clock}),
      .src_dat ({signal}),
      .src_vld ({signal}_vld),
      .dst_clk (s_axi_aclk),
      .dst_dat ({signal}_sync),
      .dst_vld ({signal}_vld_sync)
      );
'''
arc_footer = '\nendmodule'
