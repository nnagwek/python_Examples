class ObjectCounter:
    objectCount = 0

    def __init__(self):
        ObjectCounter.objectCount += 1

    @staticmethod
    def countObjects():
        print(ObjectCounter.objectCount)


o1 = ObjectCounter()
o2 = ObjectCounter()

ObjectCounter.countObjects()
