class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def show_info(self):
        print(
            f"\033[92m title is : {self.title} author is : {self.author} year is : {self.year}\033[0m",
            end=" ",
        )

    @staticmethod
    def is_valid(year):
        if 1500 <= year <= 2025:
            print("\033[94mbook is valid \033[0m")
        else:
            print("book is invalid")


b1 = Book("sateron", "naeem", 1980)
b1.show_info()
Book.is_valid(1980)
