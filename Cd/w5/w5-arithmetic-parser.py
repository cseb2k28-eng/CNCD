import ast


def is_valid(node):
    if isinstance(node, ast.Name):
        return True
    if isinstance(node, ast.Constant):
        return isinstance(node.value, int) and not isinstance(node.value, bool)
    if isinstance(node, ast.BinOp):
        return (
            type(node.op) in (ast.Add, ast.Mult)
            and is_valid(node.left)
            and is_valid(node.right)
        )
    return False


expression = input("Enter an arithmetic expression: ")

try:
    tree = ast.parse(expression, mode="eval")
    valid = is_valid(tree.body)
except SyntaxError:
    valid = False

if valid:
    print("Expression is valid.")
else:
    print("Invalid expression.")
