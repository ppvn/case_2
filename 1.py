b = 100000

for i in range(50, 0, -1):
    a = b / i
    b = b - a
    print(b)

