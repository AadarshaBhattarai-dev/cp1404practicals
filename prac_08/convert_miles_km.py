"""
CP1404 Practical
Kivy GUI program to convert miles to kilometers
Aadarsha Bhattarai
Started 15/11/2025
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

__author__ = 'Aadarsha Bhattarai'

MILES_TO_KM = 1.60934
Window.size = (420, 150)


class MilesConverterApp(App):
    km_result = StringProperty('0.000')

    def build(self):
        self.title = "Convert Miles to Kilometres"
        return Builder.load_file('convert_miles_km.kv')

    def _parse_miles(self, text):
        try:
            return float(text)
        except (ValueError, TypeError):
            return 0.0

    def handle_calculate(self, text_value=None):
        if text_value is None:
            text_value = self.root.ids.input_miles.text
        miles = self._parse_miles(text_value)
        km = miles * MILES_TO_KM
        self.km_result = f"{km:.3f}"

    def handle_increment(self, change):
        current = self._parse_miles(self.root.ids.input_miles.text)
        new_value = current + change
        if float(new_value).is_integer():
            self.root.ids.input_miles.text = str(int(new_value))
        else:
            self.root.ids.input_miles.text = str(new_value)
        self.handle_calculate(self.root.ids.input_miles.text)

    def handle_text(self, text):
        self.handle_calculate(text)

MilesConverterApp().run()
