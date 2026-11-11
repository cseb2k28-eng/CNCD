import ast

operators = {
    ast.Add: "ADD",
    ast.Sub: "SUB",
    ast.Mult: "MUL",
    ast.Div: "DIV",
}


def generate(node):
    if isinstance(node, ast.Name):
        return [f"LOAD {node.id}"]
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return [f"LOAD {node.value}"]
    if isinstance(node, ast.BinOp) and type(node.op) in operators:
        return generate(node.left) + generate(node.right) + [operators[type(node.op)]]
    raise ValueError


try:
    exp=input("Enter an arithmetic expression: ")
    code = generate(ast.parse(exp, mode="eval").body)
    print("\nGenerated Machine Code:")
    print("\n".join(code))
except (SyntaxError, ValueError):
    print("Invalid expression")
