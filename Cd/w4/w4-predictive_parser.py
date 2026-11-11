# E → T R
# R → + T R | ε
# T → F Y
# Y → * F Y | ε
# F → ( E ) | i

table = {
    ('E', 'i'): 'TR',
    ('E', '('): 'TR',
    ('R', '+'): '+TR',
    ('R', ')'): 'e',
    ('R', '$'): 'e',    
    ('T', 'i'): 'FY',
    ('T', '('): 'FY',
    ('Y', '+'): 'e',
    ('Y', ')'): 'e',
    ('Y', '$'): 'e',
    ('Y', '*'): '*FY',
    ('F', 'i'): 'i',
    ('F', '('): '(E)'
}

source = ''.join(input("Enter input: ").split())
if any(symbol not in "i+*()" for symbol in source):
    print("Invalid String")
    raise SystemExit

stack = ['$', 'E']
inp = list(source) + ['$']
i = 0

while stack:
    top = stack.pop()
    current = inp[i]

    if top == current == '$':
        print("Valid String")
        break
    elif top == current:
        i += 1
    elif (top, current) in table:
        production = table[(top, current)]
        if production != 'e':
            for x in production[::-1]:
                stack.append(x)
    else:
        print("Invalid String")
        break



# input : i+i*i