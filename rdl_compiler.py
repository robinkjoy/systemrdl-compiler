import sys
from antlr4 import *
from parser.SystemRDLLexer import SystemRDLLexer
from parser.SystemRDLParser import SystemRDLParser
from Listener import Listener
from CustomErrorListener import CustomErrorListener
#from Visitor import Visitor

def main(argv):

    if len(argv) < 2:
        exit('error: file not specified.')

    inputfile = FileStream(argv[1])

    lexer = SystemRDLLexer(inputfile)
    lexer.removeErrorListeners()
    lexer._listeners = [CustomErrorListener()]

    stream = CommonTokenStream(lexer)
    parser = SystemRDLParser(stream)
    parser._listeners = [CustomErrorListener()]

    tree = parser.root()
    listener = Listener(parser)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    listener.addrmaps[0].pprint()

if __name__ == '__main__':
    main(sys.argv)
