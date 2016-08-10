import sys
from antlr4 import *
from parser.SystemRDLLexer import SystemRDLLexer
from parser.SystemRDLParser import SystemRDLParser

def main(argv):
    input = FileStream(argv[1])
    lexer = SystemRDLLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SystemRDLParser(stream)
    tree = parser.root()

if __name__ == '__main__':
    main(sys.argv)
