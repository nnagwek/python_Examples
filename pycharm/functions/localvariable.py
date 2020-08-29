x = 123


def myfunct():
    y = 654
    print(globals()['x'])
    print(y)


# print(x)
myVar = myfunct
myVar()
myVar()
