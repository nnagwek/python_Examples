x = int(input('Enter min number: '))
y = int(input('Enter max number: '))
while x <= y:
    if x % 2 != 0:
        print(x)
    x += 1
