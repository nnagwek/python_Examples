from functools import reduce

lst = [1, 2, 7, 9, 89, 32, 47]

result = reduce(lambda x, y: x + y, lst)
print(type(result))
print(result)
