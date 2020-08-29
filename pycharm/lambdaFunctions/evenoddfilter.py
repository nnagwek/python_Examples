lst = [1, 2, 7, 9, 89, 32, 47]

result = list(filter(lambda x: x % 2 == 0, lst))
print(type(result))
for i in result:
    print(i)
