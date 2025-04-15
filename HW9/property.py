# decorator
class Person:
    def __init__(self, name, birth_day):
        self.name = name
        self.birth_day = birth_day

    # @property
    def age(self):
        from datetime import datetime as dt

        return dt.now().year - self.birth_day


def main():

    p = Person("Ali", 1987)
    print(p.age())


if __name__ == "__main__":
    main()
