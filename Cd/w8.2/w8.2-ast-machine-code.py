import ast


OPERATORS = {
    ast.Add: ("+", "ADD"),
    ast.Sub: ("-", "SUB"),
    ast.Mult: ("*", "MUL"),
    ast.Div: ("/", "DIV"),
}


def generate(node, level=0):
    indent = "  " * level
    if isinstance(node, ast.Name):
        print(f"{indent}Variable: {node.id}")
        return [f"PUSH {node.id}"]
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        print(f"{indent}Number: {node.value}")
        return [f"PUSH {node.value}"]
    if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
        symbol, instruction = OPERATORS[type(node.op)]
        print(f"{indent}Operator: {symbol}")
        left = generate(node.left, level + 1)
        right = generate(node.right, level + 1)
        return left + right + [instruction]
    raise ValueError("Use variables, numbers, and +, -, *, /.")


try:
    tree = ast.parse(input("Enter expression (example: a + b * c): "), mode="eval").body
    print("\nAbstract syntax tree:")
    instructions = generate(tree)
    print("\nStack-machine instructions:")
    print("\n".join(instructions))
except (SyntaxError, ValueError):
    print("Invalid expression")
