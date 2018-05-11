import pytest
import antlr4
import logging
from parser.antlr.SystemRDLLexer import SystemRDLLexer
from parser.antlr.SystemRDLParser import SystemRDLParser
from parser.Listener import Listener
import logger

@pytest.fixture(scope='session')
def log():
    logger.setup_logging(40, False, None)
    yield logging.getLogger()
    logging.shutdown()

def parser(rdl_string):
    inputstream = antlr4.InputStream(rdl_string)
    lexer = SystemRDLLexer(inputstream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = SystemRDLParser(stream)
    tree = parser.root()
    listener = Listener(parser)
    walker = antlr4.ParseTreeWalker()
    return walker, listener, tree


def test_parser_validation(capsys, log, error_rdl, error_msg):
    line_info = [('test', x) for x in range(1, error_rdl.count('\n')+2)]
    log.handlers[0].formatter.line_info = line_info
    walker, listener, tree = parser(error_rdl)
    with pytest.raises(SystemExit):
        walker.walk(listener, tree)
    captured = capsys.readouterr()
    assert captured.err == error_msg


def test_parser_simple_anon():
    rdl_string = '''\
    addrmap am {
        regfile {
            reg {
                field {} f1;
            } r1;
        } rf;
    };'''
    walker, listener, tree = parser(rdl_string)
    walker.walk(listener, tree)
    am = listener.addrmaps[0]
    assert am.def_id == 'am'
    assert am.parent is None
    assert am.comps[0].inst_id == 'rf'
    assert am.comps[0].parent is am
    assert am.comps[0].comps[0].inst_id == 'r1'
    assert am.comps[0].comps[0].parent is am.comps[0]
    assert am.comps[0].comps[0].comps[0].inst_id == 'f1'
    assert am.comps[0].comps[0].comps[0].parent is am.comps[0].comps[0]

def test_parser_simple_inst():
    rdl_string = '''\
    field fi {};
    reg re {
        fi f1;
    };
    regfile rgf {
        re r1;
    };
    addrmap am {
        rgf rf;
    };'''
    walker, listener, tree = parser(rdl_string)
    walker.walk(listener, tree)
    am = listener.addrmaps[0]
    assert am.def_id == 'am'
    assert am.parent is None
    assert am.comps[0].inst_id == 'rf'
    assert am.comps[0].parent is am
    assert am.comps[0].comps[0].inst_id == 'r1'
    assert am.comps[0].comps[0].parent is am.comps[0]
    assert am.comps[0].comps[0].comps[0].inst_id == 'f1'
    assert am.comps[0].comps[0].comps[0].parent is am.comps[0].comps[0]
