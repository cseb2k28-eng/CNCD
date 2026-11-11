import re
import sys

keywords = {"int", "float", "char", "if", "else", "while", "return"}
operators = {"+", "-", "*", "/", "="}
special_symbols = {";", ",", "(", ")", "{", "}"}

pattern = re.compile(
    r"(?P<comment>//[^\r\n]*|/\*[\s\S]*?\*/)"
    r"|(?P<unclosed>/\*[\s\S]*)"
    r"|(?P<space>\s+)"
    r"|(?P<token>[A-Za-z_][A-Za-z0-9_]*|[0-9]+|[+\-*/=;,(){}])"
    r"|(?P<invalid>.)"
)

print("Enter source code, then press Ctrl+Z and Enter to finish:")
source = sys.stdin.read()

for match in pattern.finditer(source):
    if match.lastgroup in {"comment", "space"}:
        continue
    if match.lastgroup == "unclosed":
        print("Error: unterminated block comment")
        break

    token = match.group()
    if token in keywords:
        print(token, "-> Keyword")
    elif token in operators:
        print(token, "-> Operator")
    elif token in special_symbols:
        print(token, "-> Special Symbol")
    elif token.isdigit():
        print(token, "-> Constant")
    elif match.lastgroup == "invalid":
        print(token, "-> Invalid")
    else:
        print(token, "-> Identifier")