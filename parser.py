import re

#31 tokens needed for the language
#Keywords, identifiers (variables), Literals (ints), OPS, Puncuators

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

    'LPAREN': r'\(', # in the group it shows as (<LPAREN>\() closes bracket
    'RPAREN': r'\)',
    'LBRACKET': r'\[', #this identifies (<LBRACKET>\[)
    'RBRACKET': r'\]',
    'COMMA': r',',

    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'NUMBER': r'\d+(\.\d+)?',
    'STRING_LITERAL': r'"([^"\\]*(\\.[^"\\]*)*)"',
    'COMMENT': r'//.*?$', #flag to skip only single line (convention)
    'WHITESPACE': r'\s+' #ignore for efficiency
}

TOKEN_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_TYPES.items())

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
            
    def tokenize(self):
        tokens = []    
        for match in re.finditer(TOKEN_REGEX, self.file, re.MULTILINE):
            kind = match.lastgroup
            value = match.group()
            self.column_number += len(value)

            if kind == 'WHITESPACE': #only to update line_num pos not perfect
                if '\n' in value:
                    self.line_number += value.count('\n')
                    self.column_number = 0
                continue

            if kind == 'COMMENT':
                self.line_number += 1
                self.column_number = 0
                continue #skip the comment

            if kind in TOKEN_TYPES: #check if kind in TOKEN_TYPES else ignore
                token = Token(kind, value, self.line_number, self.column_number)
                tokens.append(token)
            
        return tokens

#recursive decent parser

class ParseError(Exception):
    def __self__(self, pos, msg, *args):
        self.pos = pos
        self.msg = msg
        self.args = args

    def __str__(self):
        return '%s at position %s' % (self.msg % self.args, self.pos)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.end = len(self.tokens)-1
        self.cache = {}

    def parse(self):
        pass 
