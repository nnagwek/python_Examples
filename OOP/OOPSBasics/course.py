class Course:

    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings

    def averageratings(self):
        noOfRatings = len(self.ratings)
        sumOfRatings = sum(self.ratings)
        averageOfRatings = sumOfRatings / noOfRatings
        print("Average of the ratings for the course {} is {}".format(self.name, averageOfRatings))


c1 = Course('Java Course', [1, 2, 3, 4, 5])
print(c1.name)
print(c1.ratings)
c1.averageratings()

c2 = Course('Python Course', [9, 2, 4, 5])
print(c2.name)
print(c2.ratings)
c2.averageratings()
