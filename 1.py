b = 10000


def fin(x, i):
    a = x / i
    return x - a

def otkat(x):
    return x * 0.97


for state in range(50, 0, -1):
    b = fin(b, state)
    b = otkat(b)
    print(b)

