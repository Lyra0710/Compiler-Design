# Write a python program that takes in another C program as input, tokenizes it and returns which are keywords, identifiers, operators, special symbols, etc.

import ply.lex as lex

# Define token names
tokens = [
    'KEYWORD',
    'IDENTIFIER',
    'OPERATOR',
    'SPECIAL_SYMBOL',
    'CONSTANT',
]

# Define keywords
keywords = {
    'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double',
    'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register',
    'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef',
    'union', 'unsigned', 'void', 'volatile', 'while',
}

# Regular expression rules for tokens
t_KEYWORD = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_OPERATOR = r'[+\-*/%=<>!&|]+'
t_SPECIAL_SYMBOL = r'[;,(){}\[\]]+'
t_CONSTANT = r'[0-9]+'

# Ignored characters (whitespace and tabs)
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Unexpected character: '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Read input from a C program file
with open("Hello.c", "r") as file:
    c_program = file.read()

# Tokenize the C program
lexer.input(c_program)

# Token classification and printing
for token in lexer:
    if token.type == 'KEYWORD' and token.value in keywords:
        print(f"{token.value} is a keyword")
    elif token.type == 'OPERATOR':
        print(f"{token.value} is an operator")
    elif token.type == 'SPECIAL_SYMBOL':
        print(f"{token.value} is a special symbol")
    elif token.type == 'IDENTIFIER':
        print(f"{token.value} is an identifier")
    elif token.type == 'CONSTANT':
        print(f"{token.value} is a constant")
    else:
        print(f"{token.value} is an unknown token")