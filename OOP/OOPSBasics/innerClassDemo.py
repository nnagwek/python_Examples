class Car:

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def display(self):
        print("Car name ", self.name, " made in year :", self.year)

    class Engine:
        def __init__(self, number):
            self.number = number

        def startEngine(self):
            print("Engine Started with number : ", self.number)


c1 = Car("Lamb", 2019)
e1 = c1.Engine("9999")

c1.display()
e1.startEngine()
