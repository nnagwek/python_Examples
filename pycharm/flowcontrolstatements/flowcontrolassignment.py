num = int(input('Enter a number: '))
x = -1
while x <= num:
    x += 1
    if x > 100:
        break
    if x % 10 == 0:
        continue
    print(x)
