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
from io import StringIO

def main(argv):

    # parse arguments
    aparser = argparse.ArgumentParser(description='Convert SystemRDL files to outputs like RTL')
    aparser.add_argument('files', type=str, nargs='+', help='Input RDL files')
    aparser.add_argument('--perl-preproc', action='store_true',
            dest='perl_pp', help='Input RDL files')
    aparser.add_argument('--print', action='store_true',
            dest='v_print', help='Print register information')
    aparser.add_argument('--debug', action='store_true',
            dest='debug', help=argparse.SUPPRESS)
    log_level_nos = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
    log_level_names = [logging.getLevelName(i) for i in log_level_nos]
    log_levels = dict(zip(log_level_names, log_level_nos))
    aparser.add_argument('--log-level', choices=log_level_names, default='INFO',
            dest='log_level')
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

    log.handlers[0].formatter.line_info = Common.flatten(line_infos)

    # parsing
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
    if args.v_print:
        for am in listener.addrmaps:
            am.pprint()

    logging.shutdown()

if __name__ == '__main__':
    main(sys.argv)
