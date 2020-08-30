class Programmer:

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setTechnologies(self, technologies):
        self.technologies = technologies

    def getTechnologies(self):
        return self.technologies


p1 = Programmer()
p1.setName("Niket")
p1.setSalary(50000)
p1.setTechnologies("Java")

print("Hi ", p1.getName(), " has a salary of ", p1.getSalary(), " with  technologies :", p1.getTechnologies())
