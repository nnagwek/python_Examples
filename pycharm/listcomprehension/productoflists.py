a = [1, 2, 3, 4, 5]
b = [6, 9, 8, 9, 10]

# res = []
# for i in range(len(a)):
#     res.append(a[i] * b[i])
#
# print(res)

res = [a[i] * b[i] for i in range(len(a))]

print(res)
