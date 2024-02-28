import random

# UniPil case#2
# Developer: General Popov, Egor A.
# b = int(input('Выделено бюджета на 50 штатов (от 1 до 5 млн): '))

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

