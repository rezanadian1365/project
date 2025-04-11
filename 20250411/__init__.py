# __init__
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_passing(self):
        if self.grade >= 60:
            return True
        else:
            return False


s1 = Student("reza", 60)
s1.is_passing()
s1.name
s1.grade
print(f"{Student.__name__}")
print(f"{s1.name}  {s1.grade}")
