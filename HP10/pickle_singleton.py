# pickle & pickletools
import pickle

import pickletools as pt


class AppSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, theme="dark", language="English"):

        self.theme = theme
        self.language = language

    def toggle_theme(self):
        if self.theme == "dark":
            self.theme == "light"
        else:
            self.theme == "dark"
            print(f"theme changed to {self.theme}")

    def change_language(self, language):
        self.language = language
        print(f"language changed to {self.language}")


with open("AppSettings.pkl", "wb") as file:
    pickle.dump("AppSettings", file)
    print("AppSettings saved to AppSettings.pkl")


with open("AppSettings.pkl", "rb") as file:
    data = pickle.load(file)
    print("AppSettings loaded from AppSettings.pkl")
    print(data)
settings = AppSettings()
print(f"Settings:{settings.theme},{settings.language}")
settings.toggle_theme()
settings.change_language("Spanish")
print(f"settings:{settings.theme},{settings.language}")
