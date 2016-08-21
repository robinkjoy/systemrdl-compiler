import sys
from antlr4 import *
from parser.SystemRDLLexer import SystemRDLLexer
from parser.SystemRDLParser import SystemRDLParser
from Listener import Listener
#from Visitor import Visitor

def main(argv):
    inputfile = FileStream(argv[1])
    lexer = SystemRDLLexer(inputfile)
    stream = CommonTokenStream(lexer)
    parser = SystemRDLParser(stream)
    tree = parser.root()
    listener = Listener(parser)
    #visitor = Visitor()
    #print(visitor.visit(tree))
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    listener.addrmaps[0].pprint()

if __name__ == '__main__':
    main(sys.argv)
