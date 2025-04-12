# __del__
class FileManager:
    def __init__(self, jik):
        self.jik = open(jik, "w")

    def writer(self, shalgham):

        self.jik.write(shalgham)

    def __del__(self):
        self.jik.close()
        print(f"{self.jik} this time is deleting . . . ")


f = FileManager("new.txt")
f.writer("meat berger")
del f
