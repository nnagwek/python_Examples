a = [1, 2, 3, 4, 5]
b = [2, 4, 7, 9, 8]

# res = []
# for i in range(len(a)):
#     for j in range(len(b)):
#         if b[j] == a[i]:
#             res.append(b[j])


# for i in a:
#     if i in b:
#         res.append(i)
#

res = [x for x in a if x in b]
print(res)
