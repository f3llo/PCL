import sys
import re

#lexer

TOKEN_TYPES = {
    'IF': r'\bIF\b',
    'ELSE': r'\bELSE\b',
    'WHILE': r'\bWHILE\b',
    'RETURN': r'\bRETURN\b',
    'OUTPUT': r'\bOUTPUT\b',
    'INPUT': r'\bINPUT\b',
    'LOOP': r'\bloop\b',
    'METHOD': r'\bMETHOD\b',
    'END': r'\bEND\b',
    'DECLARE': r'\bDECLARE\b',
    'FROM': r'\bfrom\b',
    'TO': r'\bto\b',

    'INT': r'\bInteger\b',
    'FLOAT': r'\bFloat\b',
    'STRING': r'\bString\b',

    'NOT': r'\bNOT\b',
    'AND': r'\bAND\b',
    'OR': r'\bOR\b',

    'PLUS': r'\+',
    'MINUS': r'-',
    'MULTIPLY': r'\*',
    'DIVIDE': r'/',
    'DIV': r'//',
    'MODULUS': r'%',
    'EQUALS': r'=',
    'NOT_EQUALS': r'!=',
    'GREATER_THAN': r'>',
    'LESS_THAN': r'<',

    'LPAREN': r'\(',
    'RPAREN': r'\)',
    'LBRACKET': r'\[',
    'RBRACKET': r'\]',
    'COMMA': r',',

    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'NUMBER': r'\d+(\.\d+)?',
    'STRING_LITERAL': r'"([^"\\]*(\\.[^"\\]*)*)"',
    'COMMENT': r'//.*?$', #flag to skip only single line (convention)
    'WHITESPACE': r'\s+'
}

class Token:
    def __init__(self, _type, value, line_number, column_number):
        self.type = _type
        self.value = value
        self.line_number = line_number
        self.column_number = column_number

    def __repr__(self):
        return f"Token({self.type}, {self.value}, [{self.line_number}, {self.column_number}])"

class Lexer:
    def __init__(self, file):
        self.file = file
        self.pos = 0
        self.line_number = 1
        self.column_number = 0
        self.TOKEN_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_TYPES.items())
            
    def tokenize(self):
        tokens = []    
        for match in re.finditer(self.TOKEN_REGEX, self.file, re.MULTILINE):
            kind = match.lastgroup
            value = match.group()
            self.column_number += len(value)

            if kind in TOKEN_TYPES: #check if kind in TOKEN_TYPES else ignore
                if kind != "COMMENT" or "WHITESPACE":
                    token = Token(kind, value, self.line_number, self.column_number)
                    tokens.append(token)
                else:
                    if '\n' in value:
                        self.line_number += value.count('\n')
                    else:
                        self.line_number += 1
                    self.column_number = 0
            
        return tokens

#parser

class AST:
    pass

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Parser: #generates a AST
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def error(self):
        raise Exception("Invalid syntax")
    
    def eat(self, token_type):
        if self.current_token == token_type:
            pos += 1
        else:
            self.error()

    def factor(self):
        # INT | LPAREN expr LPAREN
        token = self.current_token
        if token.type == "INT":
            self.eat("INT")
            return Num(token)
        elif token.type == "LPAREN":
            self.eat("LPAREN")
            node = self.expr()
            self.eat("RPAREN")
            return node

    def term(self):
        # factor (*|/ factor)*
        
        node = self.factor()
        while self.current_token.type in ("MULTIPLY", "DIVIDE"):
            token = self.current_token
            if token.type == "MULTIPLY":
                self.eat("MULTIPLY")
            elif token.type == "DIVIDE":
                self.eat("DIVIDE")

            node = BinOp(node, token, self.factor())

        return node

    def expr(self):
        # term (+|- term)*
    
        node = self.term()
        while self.current_token.type in ("ADD", "SUBTRACT"):
            token = self.current_token
            if token.type == "ADD":
                self.eat("ADD")
            elif token.type == "SUBTRACT":
                self.eat("SUBTRACT")

            node = BinOp(node, token, self.term())

        return node

    def parse(self):
        return self.expr()

#interpreter

class NodeVisitor():
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

class Interpreter:
    pass



#main execution starts here

try:
    file = open(sys.argv[1], "r")
except FileNotFoundError:
    print("No such file in directory")
    sys.exit()

lexer = Lexer(file.read())
tokens = lexer.tokenize()

parser = Parser(tokens)
parser.parse_arithmatic()

