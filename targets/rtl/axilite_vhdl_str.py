libraries = '''library IEEE;
use ieee.std_logic_1164.all;
'''
entity_header = '''
entity axilite_reg_if is
  generic (
    C_S_AXI_DATA_WIDTH : integer := {};
    C_S_AXI_ADDR_WIDTH : integer := {}
    );
  port (
'''
st_in = '    {name} : in  std_logic;\n'
st_out = '    {name} : out std_logic;\n'
sv_in = '    {name} : in  std_logic_vector({width} downto 0);\n'
sv_out = '    {name} : out std_logic_vector({width} downto 0);\n'
clock_comment = '    -- Clocks\n'
pl_port_comment = '    -- PL Ports\n'
axi_ports_end = '''    -- AXILite Signal
    s_axi_aclk : in  std_logic;
    s_axi_areset : in  std_logic;
    s_axi_awaddr : in  std_logic_vector(C_S_AXI_ADDR_WIDTH-1 downto 0);
    s_axi_awprot : in  std_logic_vector(2 downto 0);
    s_axi_awvalid : in  std_logic;
    s_axi_awready : out std_logic;
    s_axi_wdata : in  std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0);
    s_axi_wstrb : in  std_logic_vector((C_S_AXI_DATA_WIDTH/8)-1 downto 0);
    s_axi_wvalid : in  std_logic;
    s_axi_wready : out std_logic;
    s_axi_bresp : out std_logic_vector(1 downto 0);
    s_axi_bvalid : out std_logic;
    s_axi_bready : in  std_logic;
    s_axi_araddr : in  std_logic_vector(C_S_AXI_ADDR_WIDTH-1 downto 0);
    s_axi_arprot : in  std_logic_vector(2 downto 0);
    s_axi_arvalid : in  std_logic;
    s_axi_arready : out std_logic;
    s_axi_rdata : out std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0);
    s_axi_rresp : out std_logic_vector(1 downto 0);
    s_axi_rvalid : out std_logic;
    s_axi_rready : in  std_logic
    );
end entity axilite_reg_if;

architecture arch_imp of axilite_reg_if is
'''

components = '''
  component cdc_sync
    generic (
      WIDTH      : natural := 1;
      WITH_VLD   : boolean := false;
      SRC_PER_NS : real    := 5.0;
      DST_PER_NS : real    := 8.0;
      DAT_IS_REG : boolean := true;
      IS_PULSE   : boolean := false
      );
    port (
      src_clk : in  std_logic;
      src_dat : in  std_logic_vector (WIDTH-1 downto 0);
      src_vld : in  std_logic;
      dst_clk : in  std_logic;
      dst_dat : out std_logic_vector (WIDTH-1 downto 0);
      dst_vld : out std_logic
      );
  end component cdc_sync;
'''

constants = '''
  constant ADDR_LSB          : integer := (C_S_AXI_DATA_WIDTH/32)+ 1;
  constant OPT_MEM_ADDR_BITS : integer := {};
'''

internal_signals = '''
  -- AXI4LITE signals
  signal axi_awaddr  : std_logic_vector(C_S_AXI_ADDR_WIDTH-1 downto 0) := (others => '0');
  signal axi_awready : std_logic := '0';
  signal axi_wready  : std_logic := '0';
  signal axi_bresp   : std_logic_vector(1 downto 0) := (others => '0');
  signal axi_bvalid  : std_logic := '0';
  signal axi_araddr  : std_logic_vector(C_S_AXI_ADDR_WIDTH-1 downto 0) := (others => '0');
  signal axi_arready : std_logic := '0';
  signal axi_rdata   : std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0) := (others => '0');
  signal axi_rresp   : std_logic_vector(1 downto 0) := (others => '0');
  signal axi_rvalid  : std_logic := '0';

  signal slv_reg_rden : std_logic := '0';
  signal slv_reg_wren : std_logic := '0';
  signal reg_data_out : std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0) := (others => '0');

'''

reg_signal = '  signal {name} : std_logic_vector({width} downto 0) := (others => \'0\');\n'

begin_io_assgns_axi_logic = '''
begin

  -- I/O Connections assignments
  s_axi_awready <= axi_awready;
  s_axi_wready  <= axi_wready;
  s_axi_bresp   <= axi_bresp;
  s_axi_bvalid  <= axi_bvalid;
  s_axi_arready <= axi_arready;
  s_axi_rdata   <= axi_rdata;
  s_axi_rresp   <= axi_rresp;
  s_axi_rvalid  <= axi_rvalid;

  process (s_axi_aclk)
  begin
    if rising_edge(s_axi_aclk) then
      if s_axi_areset = '1' then
        axi_awready <= '0';
      else
        if axi_awready = '0' and s_axi_awvalid = '1' and s_axi_wvalid = '1' then
          axi_awready <= '1';
        else
          axi_awready <= '0';
        end if;
      end if;
    end if;
  end process;

  process (s_axi_aclk)
  begin
    if rising_edge(s_axi_aclk) then
      if s_axi_areset = '1' then
        axi_awaddr <= (others => '0');
      else
        if axi_awready = '0' and s_axi_awvalid = '1' and s_axi_wvalid = '1' then
          axi_awaddr <= s_axi_awaddr;
        end if;
      end if;
    end if;
  end process;

  process (s_axi_aclk)
  begin
    if rising_edge(s_axi_aclk) then
      if s_axi_areset = '1' then
        axi_wready <= '0';
      else
        if axi_wready = '0' and s_axi_wvalid = '1' and s_axi_awvalid = '1' then
          axi_wready <= '1';
        else
          axi_wready <= '0';
        end if;
      end if;
    end if;
  end process;

  slv_reg_wren <= axi_wready and s_axi_wvalid and axi_awready and s_axi_awvalid;
'''

axi_write_header = '''
  process (s_axi_aclk)
    variable loc_addr : std_logic_vector(OPT_MEM_ADDR_BITS downto 0);
  begin
    if rising_edge(s_axi_aclk) then
      if s_axi_areset = '1' then'''
axi_write_reset_reg = '\n'+'  '*4+'{name}({msb} downto {lsb}) <= (others => \'0\');'
axi_write_else_header = '''
      else
        loc_addr := axi_awaddr(ADDR_LSB + OPT_MEM_ADDR_BITS downto ADDR_LSB);
        if slv_reg_wren = '1' then'''
axi_write_assign = '''
          if loc_addr = b"{val}" then
            for i in 0 to (C_S_AXI_DATA_WIDTH/8-1) loop
              if s_axi_wstrb(i) = '1' then
                {name}(i*8+7 downto i*8) <= s_axi_wdata(i*8+7 downto i*8);
              end if;
            end loop;'''
axi_write_assign_else = '\n          else'
axi_write_assign_end = '\n          end if;'
axi_write_else = '\n        else'
axi_sclr_part1 = ''
axi_sclr_part2 = ' & '
axi_sclr_part3 = '({} downto {})'
axi_sclr_part4 = '"{val}"'
axi_sclr_part5 = ';'
axi_write_footer = '''
        end if;
      end if;
    end if;
  end process;
'''
axi_logic2 = '''

  process (s_axi_aclk)
  begin
    if rising_edge(s_axi_aclk) then
      if s_axi_areset = '1' then
        axi_bvalid <= '0';
        axi_bresp  <= "00";
      else
        if axi_awready = '1' and s_axi_awvalid = '1' and axi_wready = '1'
          and s_axi_wvalid = '1' and axi_bvalid = '0' then
          axi_bvalid <= '1';
          axi_bresp  <= "00";
        elsif s_axi_bready = '1' and axi_bvalid = '1' then
          axi_bvalid <= '0';
        end if;
      end if;
    end if;
  end process;

  process (s_axi_aclk)
  begin
    if rising_edge(s_axi_aclk) then
      if s_axi_areset = '1' then
        axi_arready <= '0';
        axi_araddr  <= (others => '1');
      else
        if axi_arready = '0' and s_axi_arvalid = '1' then
          axi_arready <= '1';
          axi_araddr  <= s_axi_araddr;
        else
          axi_arready <= '0';
        end if;
      end if;
    end if;
  end process;

  process (s_axi_aclk)
  begin
    if rising_edge(s_axi_aclk) then
      if s_axi_areset = '1' then
        axi_rvalid <= '0';
        axi_rresp  <= "00";
      else
        if axi_arready = '1' and s_axi_arvalid = '1' and axi_rvalid = '0' then
          axi_rvalid <= '1';
          axi_rresp  <= "00";           -- 'OKAY' response
        elsif axi_rvalid = '1' and s_axi_rready = '1' then
          axi_rvalid <= '0';
        end if;
      end if;
    end if;
  end process;

  slv_reg_rden <= axi_arready and s_axi_arvalid and (not axi_rvalid);
'''
reg_data_out_header = '''
  process ({sens}axi_araddr, s_axi_areset, slv_reg_rden)
    variable loc_addr : std_logic_vector(OPT_MEM_ADDR_BITS downto 0);
  begin
    if s_axi_areset = '1' then
      reg_data_out <= (others => '0');
    else
      loc_addr := axi_araddr(ADDR_LSB + OPT_MEM_ADDR_BITS downto ADDR_LSB);
      case loc_addr is'''
reg_data_out_when = '''
        when b"{num_bin}" =>
          reg_data_out <= {name};'''
reg_data_out_footer_axi_logic = '''
        when others =>
          reg_data_out <= (others => '0');
      end case;
    end if;
  end process;

  process(s_axi_aclk) is
  begin
    if rising_edge (s_axi_aclk) then
      if s_axi_areset = '1' then
        axi_rdata <= (others => '0');
      else
        if slv_reg_rden = '1' then
          axi_rdata <= reg_data_out;
        end if;
      end if;
    end if;
  end process;
'''
ctrl_sig_assgns_header = '\n  -- Assign registers to control signals\n'
ctrl_sig_assgns = '  {} <= {}({} downto {});\n'
ctrl_sig_assgns_1bit = '  {} <= {}({});\n'
sts_sig_assgns_header = '''
  -- Assign status signals to registers
  process(s_axi_aclk)
    variable loc_addr : std_logic_vector(OPT_MEM_ADDR_BITS downto 0);
  begin
    if rising_edge(s_axi_aclk) then
      if s_axi_areset = '1' then'''
sts_sig_assgns_reset = '\n        {} <= (others => \'0\');'
sts_sig_assgns_reset_else = '''
      else
        loc_addr := axi_awaddr(ADDR_LSB + OPT_MEM_ADDR_BITS downto ADDR_LSB);'''
sts_sig_assgns_no_clr = '\n        {reg_name}({msb} downto {lsb}) <= {signal};'
sts_sig_assgns_no_clr_1bit = '\n        {reg_name}({msb}) <= {signal};'
sts_sig_assgns_with_clr = '''
        if {signal_valid} = '1' then
          {reg_name}({msb} downto {lsb}) <= {signal};
        elsif slv_reg_wren = '1' and loc_addr = b"{addr_bin}"
          and S_AXI_WSTRB({strb_lsb} downto {strb_msb}) = "{strb_1s}" then
          {reg_name}({msb} downto {lsb}) <= (others => \'0\');
        else
          {reg_name}({msb} downto {lsb}) <= {reg_name}({msb} downto {lsb});
        end if;'''
sts_sig_assgns_with_clr_1bit = '''
        if {signal_valid} = '1' then
          {reg_name}({msb}) <= {signal};
        elsif slv_reg_wren = '1' and loc_addr = b"{addr_bin}"
          and S_AXI_WSTRB({strb_lsb} downto {strb_msb}) = "{strb_1s}" then
          {reg_name}({msb}) <= \'0\';
        else
          {reg_name}({msb}) <= {reg_name}({msb});
        end if;'''
sts_sig_assgns_footer = '''
      end if;
    end if;
  end process;
'''
arc_footer = '\nend arch_imp;'
