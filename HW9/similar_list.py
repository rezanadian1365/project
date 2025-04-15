# list
class Mylist:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value


lst = Mylist([1, 2, 3, 4, 5])
lst.__setitem__(0, 5)
print(lst.__getitem__(0))  # Output: 5
