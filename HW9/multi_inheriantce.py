class Fly:

    print("i can fly")


class Swim:
    print("i can swim")


class Duck(Fly, Swim):

    pass


d1 = Duck()
