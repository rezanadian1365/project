# singleton
# enheritance
# classmethod
# instancemethod
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
            print("class method is runnung")
        return cls._instance

    def __init__(self):
        print("\/instance method is running\/")


akbar = Singleton()
print("*" * 30)
asghar = Singleton()
print("*" * 30)
javad = Singleton()
answer = akbar is asghar
print("*" * 30)
print(f"           {answer}")
id(akbar) == id(asghar)
