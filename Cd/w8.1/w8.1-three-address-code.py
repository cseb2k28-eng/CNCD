import ast


OPERATORS = {ast.Add: "+", ast.Sub: "-", ast.Mult: "*", ast.Div: "/"}


def generate(node, code):
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return str(node.value)
    if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
        left = generate(node.left, code)
        right = generate(node.right, code)
        temporary = f"t{len(code) + 1}"
        code.append(f"{temporary} = {left} {OPERATORS[type(node.op)]} {right}")
        return temporary
    raise ValueError("Use variables, numbers, and +, -, *, /.")


try:
    assignment = ast.parse(input("Enter assignment (example: x = a + b): ")).body[0]
    if not isinstance(assignment, ast.Assign) or len(assignment.targets) != 1:
        raise ValueError
    if not isinstance(assignment.targets[0], ast.Name):
        raise ValueError

    code = []
    result = generate(assignment.value, code)
    code.append(f"{assignment.targets[0].id} = {result}")
    print("\nThree-address code:")
    print("\n".join(code))
except (SyntaxError, ValueError, IndexError):
    print("Invalid assignment or expression")
