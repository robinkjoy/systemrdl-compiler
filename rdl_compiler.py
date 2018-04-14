import sys
import antlr4
import argparse
import logging
from parser.antlr.SystemRDLLexer import SystemRDLLexer
from parser.antlr.SystemRDLParser import SystemRDLParser
from parser.Listener import Listener
from parser.CustomErrorListener import CustomErrorListener
from parser.preproc import preproc
import logger
import Common
import targets.rtl.rtl_axilite_gen as rtl_gen


def main():
    # parse arguments
    aparser = argparse.ArgumentParser(description='Convert SystemRDL files to outputs like RTL')
    aparser.add_argument('files', type=str, nargs='+', help='Input RDL files')
    aparser.add_argument('--perl-preproc', action='store_true',
                         dest='perl_pp', help='Enable perl preprocessing')
    aparser.add_argument('--print', action='store_true',
                         dest='v_print', help='Print register information')
    aparser.add_argument('--lang', choices=['verilog', 'vhdl'], default='vhdl',
                         dest='lang', help='Select target language')
    log_level_nos = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
    log_level_names = [logging.getLevelName(i) for i in log_level_nos]
    log_levels = dict(zip(log_level_names, log_level_nos))
    aparser.add_argument('--log-level', choices=log_level_names, default='INFO',
                         dest='log_level', help='Select log level')
    aparser.add_argument('--debug', action='store_true',
                         dest='debug', help=argparse.SUPPRESS)
    args = aparser.parse_args()

    # setup logger
    logger.setup_logging(log_levels[args.log_level], args.debug)
    log = logging.getLogger()

    # preprocessing
    log.info('Start preprocessing..')
    data = ''
    line_infos = []
    for fn in args.files:
        (data_pp, ln) = preproc(fn, args.perl_pp)
        data += data_pp
        line_infos += ln
    log.info('Preprocessing done.')

    log.handlers[0].formatter.line_info = Common.flatten(line_infos, [])

    # parsing
    log.info('Start parsing..')
    inputfile = antlr4.InputStream(data)

    lexer = SystemRDLLexer(inputfile)
    lexer.removeErrorListeners()
    lexer._listeners = [CustomErrorListener()]

    stream = antlr4.CommonTokenStream(lexer)
    parser = SystemRDLParser(stream)
    parser._listeners = [CustomErrorListener()]

    tree = parser.root()
    listener = Listener(parser)
    walker = antlr4.ParseTreeWalker()
    walker.walk(listener, tree)
    log.info('Parsing done.')
    for am in listener.addrmaps:
        am.populate_addresses(0, 'regalign')
        last_addr = am.validate_addresses()
        log.info(f'{am.def_id} assigned address space till 0x{last_addr:x}')
        if args.v_print:
            am.pprint()
        log.info(f'Generating RTL for AddrMap {am.def_id}..')
        rtl_gen.generate_rtl(args.lang, am, last_addr)

    log.info('Done.')
    logging.shutdown()


if __name__ == '__main__':
    main()
