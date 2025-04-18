# class add R&D __call__
class BaseCalculate:
    def __init__(self, total: int = 0):
        self.total = total


class Add(BaseCalculate):

    def __call__(self, args: int):
        if not isinstance(args, int):
            raise TypeError("args just intiger")
        else:
            return Add(self.total + args)

    def __str__(self):
        return f"{self.total}"


# a = Add()
print(Add(0)(1)(2)(3)(100))
