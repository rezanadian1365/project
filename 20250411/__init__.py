# __init__
class Student:
    def __inuit__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_passing(self):
        if self.grade >= 60:
            return True
        else:
            return False


s1 = Student("reza", 99)
s1.is_passing()
