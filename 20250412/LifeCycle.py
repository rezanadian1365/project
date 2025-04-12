class Person:
    def __init__(self, name):
        self.name = name
        print("constructor is create Obj")

    def say(self):
        print(f" hellooooo{self.name}")

    def __del__(self):
        print("destructor is delete obj")


p1 = Person("kali")
p1.say()
del p1
