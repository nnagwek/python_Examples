def stringDecor(functio):
    def inner(name):
        result = functio(name)
        return result + ' How are you?'

    return inner


@stringDecor
def nameret(name):
    return "Hello " + name


print(nameret('mamu'))
