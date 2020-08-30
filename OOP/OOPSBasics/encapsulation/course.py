# Encapsulation Example
class Course:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setDescription(self, description):
        self.description = description;

    def getDescription(self):
        return self.description


c1 = Course()
c1.setName("Python")
c1.setDescription("Core & Advanced Python")
print("Course Name : ", c1.getName())
print("Course Description : ", c1.getDescription())
