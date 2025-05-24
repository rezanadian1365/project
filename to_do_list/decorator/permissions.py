class Animals:
    def __init__(self, animal_type, name, age):
        self.animal_type = animal_type
        self.name = name
        self.age = age

    def __str__(self):
        return f"Animal Type: {self.animal_type},Name:{self.name},Age:{self.age}"


class Sound(Animals):
    def __init__(self, sound, animal_type, name, age):
        super().__init__(animal_type, name, age)
        self.sound = sound


a = Animals("dog", "jim", 2)
print(a.__str__())
