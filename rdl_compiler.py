import sys
import antlr4
from parser.SystemRDLLexer import SystemRDLLexer
from parser.SystemRDLParser import SystemRDLParser
from Listener import Listener
from CustomErrorListener import CustomErrorListener


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
