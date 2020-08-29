import sys

lst = sys.argv
i = 0
prod = 1
while i < len(lst)-1:
    i += 1
    prod *= int(lst[i])

print("Product of numbers is ", prod)
