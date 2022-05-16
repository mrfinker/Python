from unittest import TextTestResult
import kivy

from kivy.app import App
from kivy.uix.label import Label

class MyfirstApp(App):
    def build(self):
        return Label(text = "Hello word")

MyfirstApp().run()