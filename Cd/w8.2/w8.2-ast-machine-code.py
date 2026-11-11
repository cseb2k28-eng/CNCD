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
        return [f"{indent}Variable: {node.id}"], [f"PUSH {node.id}"]
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return [f"{indent}Number: {node.value}"], [f"PUSH {node.value}"]
    if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
        symbol, instruction = OPERATORS[type(node.op)]
        left_tree, left_code = generate(node.left, level + 1)
        right_tree, right_code = generate(node.right, level + 1)
        tree = [f"{indent}Operator: {symbol}"] + left_tree + right_tree
        code = left_code + right_code + [instruction]
        return tree, code
    raise ValueError("Use variables, numbers, and +, -, *, /.")


try:
    tree = ast.parse(input("Enter expression (example: a + b * c): "), mode="eval").body
    ast_lines, instructions = generate(tree)
    print("\nAbstract syntax tree:")
    print("\n".join(ast_lines))
    print("\nStack-machine instructions:")
    print("\n".join(instructions))
except (SyntaxError, ValueError):
    print("Invalid expression")
