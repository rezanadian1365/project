# class Add:
class Add:
    def __init__(self, *args: int):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("args just intiger")
        self.args = args

    def add(self):

        res = sum(self.args)
        print(f"{res}")


a = Add(2, 5, 3, 4)
print(a.add())
