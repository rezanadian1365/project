class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.content = ""

    def create_file(self):
        with open(self.filename, "w") as file:
            file.write("this is my first file \n")

    def read_file(self, filename):
        with open(filename, "r") as filename:
            self.content = filename.read()
        print(self.content)

    def __del__(self):
        print("this file is Deldeting . . . ")


f1 = FileHandler("log.txt")
f1.create_file()
f1.read_file("log.txt")
