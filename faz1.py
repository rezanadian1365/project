class Movie:

    def __init__(self, title, director, year):
        self.title = title
        self.dierctor = director
        self.year = year

    def info(self):
        print(f"title= {self.title}  director= {self.dierctor} year= {self.year}")


m1 = Movie("gol", "reza", 1988)
inf = m1.info()
print(inf)
