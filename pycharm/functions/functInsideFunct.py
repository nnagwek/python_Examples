def myfunction(name):
    def mynewfunct():
        return " Hello "

    return mynewfunct() + name


myStr = myfunction('niket')
print(myStr)
