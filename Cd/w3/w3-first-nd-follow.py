# grammar
# E=TR
# R=+TR|e
# T=FY
# Y=*FY|e
# F=(E)|i

grammar = {
    'E': ['TR'],
    'R': ['+TR', 'e'],
    'T': ['FY'],
    'Y': ['*FY', 'e'],
    'F': ['(E)', 'i']
}

first = {}
follow = {}

for x in grammar:
    first[x] = set()
    follow[x] = set()

def FIRST(x):
    if x not in grammar:
        return {x}

    if first[x]:
        return first[x]

    for p in grammar[x]:
        if p == 'e':
            first[x].add('e')
        else:
            for c in p:
                f = FIRST(c)
                first[x] |= f - {'e'}
                if 'e' not in f:
                    break
            else:
                first[x].add('e')

    return first[x]

for x in grammar:
    FIRST(x)

follow['E'].add('$')

changed = True
while changed:
    changed = False
    for x in grammar:
        for p in grammar[x]:
            for i, c in enumerate(p):
                if c in grammar:
                    old = len(follow[c])
                    if i + 1 < len(p):
                        f = FIRST(p[i + 1])
                        follow[c] |= f - {'e'}
                        if 'e' in f:
                            follow[c] |= follow[x]
                    else:
                        follow[c] |= follow[x]
                    if len(follow[c]) > old:
                        changed = True

for x in grammar:
    print("FIRST(", x, ") =", first[x])

print()

for x in grammar:
    print("FOLLOW(", x, ") =", follow[x])