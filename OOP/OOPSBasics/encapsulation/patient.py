class Patient:

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setDescr(self, descr):
        self.descr = descr

    def getDescr(self):
        return self.descr


p1 = Patient()
p1.setId(2)
p1.setName("Mamu")
p1.setDescr("Hi how are you")

print(p1.getId())
print(p1.getName())
print(p1.descr)
