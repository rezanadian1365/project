class AccuntBank:
    def __init__(self, name, balance=0):
        self.__name = name
        self.__balance = balance

    def get_balance(self):
        print(f"is Balance : {self.__balance}")

    def get_name(self):
        print(f" is accunt name : {self.__name}")

    def deposit(self, deposit):
        self.__balance += deposit

    def withall(self, withrall):
        if self.__balance >= withrall:
            self.__balance -= withrall


acc = AccuntBank("Reza Nadian", 204000000)
acc.get_balance()
acc.get_name()
acc.withall(24000000)
acc.get_balance()
