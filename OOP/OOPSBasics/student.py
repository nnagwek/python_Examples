class Student:
    major = "CSE"

    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name


s1 = Student(1, "nik")
print(s1.major)
print(s1.rollno)
print(s1.name)
print(Student.major)
