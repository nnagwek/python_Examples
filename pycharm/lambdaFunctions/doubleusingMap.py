lst = [1, 2, 7, 9, 89, 32, 47]

result = list(map(lambda x: x * 2, lst))

print(type(result))

for i in result:
    print(i)
