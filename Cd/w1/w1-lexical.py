import re

keywords = {"int", "float", "char", "if", "else", "while", "return"}

operators = {"+", "-", "*", "/", "="}

special_symbols = {";", ",", "(", ")", "{", "}"}

s = input("Enter expression: ")

tokens = re.findall(r'[A-Za-z_][A-Za-z0-9_]*|[0-9]+|[+\-*/=;,(){}]', s)

for token in tokens:
    if token in keywords:
        print(token, "-> Keyword")
    elif token in operators:
        print(token, "-> Operator")
    elif token in special_symbols:
        print(token, "-> Special Symbol")
    elif token.isdigit():
        print(token, "-> Constant")
    else:
        print(token, "-> Identifier")