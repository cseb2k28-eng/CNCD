import ast
import operator


OPERATIONS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


def calculate(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in OPERATIONS:
        left = calculate(node.left)
        right = calculate(node.right)
        return OPERATIONS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = calculate(node.operand)
        return value if isinstance(node.op, ast.UAdd) else -value
    raise ValueError("Unsupported expression")


try:
    expression = input("Enter arithmetic expression: ")
    result = calculate(ast.parse(expression, mode="eval").body)
    print("Result:", result)
except (SyntaxError, ValueError, ZeroDivisionError):
    print("Invalid arithmetic expression")
