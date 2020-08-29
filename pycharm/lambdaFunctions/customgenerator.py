def customegen(x, y):
    while x < y:
        yield x * 2
        x += 1


result = customegen(1, 10)

for i in result: print(i)
