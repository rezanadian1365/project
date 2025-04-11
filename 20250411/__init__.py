# __init__
class Student:
    def __init__(self, name, grade, gen):
        self.name = name
        self.grade = grade
        self.gen = gen

    def is_passing(self):
        if self.grade >= 60:
            return "passed"
        else:
            return "unpassed"

    def gender(self):
        if self.gen == "f":
            return f"{self.name} is Female"
        elif self.gen == "m":
            return f"{self.name} is Male"


s1 = Student("reza", 60, "m")
print(s1.is_passing())
print(s1.name)
print("*" * 40)
s1.gender()
print(f"{Student.__name__}")
print(f"{s1.name}  {s1.grade}")
