# UniPil case#2
# Developer: student Popov, Egor A.

import random
import locals

b = int(input(locals.Budget))


def otkat(x):
    return x * 0.97


def fin(x, i):
    a = x / i
    return x - a


def tax(b):
    a = random.randint(1, 10)
    if a == 1:
        business = 10000000
        age = random.randint(20, 40)
        income = business * age
        if b - income > 0:
            return b - income
        else:
            return b
    else:
        return b


for state in range(50, 0, -1):
    b = fin(b, state)
    b = otkat(b)
    b = tax(b)
    print(f'State {state} receives {round(b)} $')
