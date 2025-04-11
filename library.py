class Library:
    def __init__(self, name, location, opening_hours):
        self.name = name
        self.location = location
        self.opening_hours = opening_hours

    # name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Library name must be a non-empty string.")
        self._name = value.strip()

    # location property
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Location must be a non-empty string.")
        self._location = value.strip()

    # opening_hours property
    @property
    def opening_hours(self):
        return self._opening_hours

    @opening_hours.setter
    def opening_hours(self, value):
        if not isinstance(value, str) or "-" not in value:
            raise ValueError(
                "Opening hours must be a string in the format 'HH:MM - HH:MM'."
            )
        self._opening_hours = value.strip()

    def __str__(self):
        return f"Library(name={self.name}, location={self.location}, opening_hours={self.opening_hours})"


class Shelf(list):
    def __init__(self, shelf_number, category_id, unique, max_total_pages):
        super().__init__()
        self.shelf_number = shelf_number
        self.category_id = category_id
        self.unique = f"{shelf_number}-{category_id}"
        self.max_total_pages = max_total_pages
        self.current_total_pages = 0

    def total_pages(self):
        return self.current_total_pages

    def add_book(self, book):
        if self.current_total_pages + book.pages > self.max_total_pages:
            raise ValueError("Cannot add book: shelf capacity exceeded.")
        self.append(book)
        self.current_total_pages += book.pages

    def __str__(self):
        return (
            f"Shelf {self.unique} - {len(self)} books, {self.total_pages()} total pages"
        )


class Librarian:
    def __init__(self, library):
        self.library = library
        self.categories = []

    def add_category(self, category):
        if category in self.categories:
            raise ValueError("Category already exists.")
        self.categories.append(category)

    def search_book(self, books, search_type, value):
        result = []
        for book in books:
            if getattr(book, search_type) == value:
                result.append(book)
        return result

    def place_book_in_shelf(self, book, shelf):
        if isinstance(shelf, Shelf):
            shelf.add_book(book)
        else:
            raise ValueError("Shelf not found.")


class Category:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __len__(self):
        return sum(book.pages for book in self.books)


class Book:
    def __init__(self, book_id, title, author, category, pages, price):
        self.book_id = book_id
        self.title = title
        self.author = author  # Author instance
        self.category = category  # Category instance
        self.pages = pages
        self.price = price

    def __str__(self):
        return f"Book {self.title} by {self.author.name}, {self.pages} pages"


class Author:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


import pickle


class Filehandler:

    @staticmethod
    def save(obj, filename):
        with open(filename, "wb") as f:
            pickle.dump(obj, f)

    @staticmethod
    def load(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)


shelf1 = Shelf(1, "Fiction", None, 500)
shelf2 = Shelf(2, "Science", None, 400)

print(shelf1.unique)
print(shelf2.unique)

author1 = Author("J.K. Rowling")
book1 = Book(1, "Harry Potter", author1, "Fantasy", 300, 20)
book2 = Book(2, "The Casual Vacancy", author1, "Fiction", 500, 25)


category1 = Category("Fiction")
category1.add_book(book1)
category1.add_book(book2)


print(len(category1))
