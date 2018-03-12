import sys
import antlr4
from parser.antlr.SystemRDLLexer import SystemRDLLexer
from parser.antlr.SystemRDLParser import SystemRDLParser
from parser.Listener import Listener
from parser.CustomErrorListener import CustomErrorListener


def main(argv):

    if len(argv) < 2:
        exit('error: file not specified.')

    inputfile = antlr4.FileStream(argv[1])

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
    listener.addrmaps[0].pprint()

if __name__ == '__main__':
    main(sys.argv)
