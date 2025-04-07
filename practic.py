class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ShiaMuslim(Person):
    def __init__(self, name, age, knows_about_ashura):
        self.knows_about_ashura = knows_about_ashura
        super().__init__(name, age)

    def can_attend(self):
        if self.age >= 15 and self.knows_about_ashura == "yes":
            print("you can invite to Ashoora")
        else:
            print("you are not invite to Ashoora")


p1 = ShiaMuslim("ali", 18, "yes")
p2 = ShiaMuslim("reza", 15, "no")
p3 = ShiaMuslim("sara", 12, "yes")
p1.can_attend()
p2.can_attend()
p3.can_attend()
