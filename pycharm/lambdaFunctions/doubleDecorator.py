def doubleDecorator(fun):
    def inner():
        result = fun()
        return result * 2

    return inner


@doubleDecorator
def functio():
    return 15


# # returns a inner function
# result = doubleDecorator(functio)
# print(result())

print(functio())
