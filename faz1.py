class Movie:

    def __init__(self, title: str, director: str, year: int, rating: float):
        self.title = title
        self.dierctor = director
        self.year = year
        self.rating = rating

    def info(self):
        print(
            f"title= {self.title}  director= {self.dierctor} year= {self.year}, rate={self.rating}",
        )

    def product(self):
        if self.year > 2000:
            print(f"this movie {self.title} is new")
        else:
            print(f"this move {self.title} is classic")

    def new_rating(self, new_rate):

        if 0 <= new_rate <= 10:
            self.rating = new_rate
            print(f"new rating for {self.title} sucsses , newrating is: {self.rating}")

        else:
            print("Invalid rating! Must be between 0 and 10")


move1 = Movie("brakingbad", "cris", 2020, 9.7)
move2 = Movie("punisher", "mickel", 1900, 8.2)
move2.info()
move1.info()
move1.product()
move2.product()
move1.new_rating(9.8)
move2.new_rating(2)
move2.info()
move1.info()
