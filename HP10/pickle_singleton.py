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
