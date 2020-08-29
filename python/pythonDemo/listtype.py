lst=[10,20,'niket',-2,4.5]
print(type(lst))
print(lst)

# functions of lists
print(lst[2])
print(lst[2:5])
print(len(lst))

lst.append(40)
lst.remove('niket')
lst.reverse()
del(lst[1])

print(lst)

# lst.clear()
# print(lst)

print(max(lst))
print(min(lst))

lst.insert(3 ,99)
print(lst)

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)