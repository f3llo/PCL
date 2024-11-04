import sys
import lexer
import parser

#pc is the main code used when interpreting code
#it expects a argument in the form of a filepath to read
#any arguments can then be given

try:
    file = open(sys.argv[1], "r")
except FileNotFoundError:
    print("No such file in directory")
    sys.exit()

lexer = lexer.Lexer(file.read())
tokens = lexer.tokenize()

parser = parser.Parser(tokens)
parser.parse_arithmatic()


