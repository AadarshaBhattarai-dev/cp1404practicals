"""
CP1404 Practical
Kivy GUI program to square a number
Aadarsha Bhattarai
Started 15/11/2025
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Aadarsha Bhattarai'

class SquareNumberApp(App):
    def build(self):
        Window.size = (400, 200)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass

SquareNumberApp().run()
