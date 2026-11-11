import ast

count = 0
operators = {
    ast.Add: "+",
    ast.Sub: "-",
    ast.Mult: "*",
    ast.Div: "/",
}


def tac(node):
    global count

    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return str(node.value)
    if not isinstance(node, ast.BinOp) or type(node.op) not in operators:
        raise ValueError

    left = tac(node.left)
    right = tac(node.right)
    count += 1
    temp = f"t{count}"
    print(f"{temp} = {left} {operators[type(node.op)]} {right}")
    return temp


try:
    expression = input("Enter expression: ")
    result = tac(ast.parse(expression, mode="eval").body)
    print("Result:", result)
except (SyntaxError, ValueError):
    print("Invalid expression")
