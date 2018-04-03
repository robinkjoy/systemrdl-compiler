import sys
import antlr4
import argparse
from parser.antlr.SystemRDLLexer import SystemRDLLexer
from parser.antlr.SystemRDLParser import SystemRDLParser
from parser.Listener import Listener
from parser.CustomErrorListener import CustomErrorListener
from parser.preproc import perl_preproc


def main(argv):

    aparser = argparse.ArgumentParser(description='Convert SystemRDL files to outputs like RTL')
    aparser.add_argument('files', type=str, nargs='+', help='Input RDL files')
    aparser.add_argument('--perl-preproc', action='store_true',
            dest='pp_enable', help='Input RDL files')
    aparser.add_argument('--print', action='store_true',
            dest='v_print', help='Print register information')

    args = aparser.parse_args()

    stream = ''
    for fn in args.files:
        if args.pp_enable:
            (pp, ln) = perl_preproc(fn)
        else:
            pp = open(fn).read()
        stream += pp

    inputfile = antlr4.InputStream(stream)

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

if __name__ == '__main__':
    main(sys.argv)
