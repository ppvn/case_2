b = 100000


def fin(x, i):
    a = x / i
    return x - a

for state in range(50, 0, -1):
    b = fin(b, state)
    print(b)

