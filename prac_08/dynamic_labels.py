"""
CP1404 Practical
Aadarsha Bhattarai
Started 15/11/2025
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsCleanApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.people = ["Alice", "Josh", "Harry", "Tobi", "Ethan", "Vik"]

    def build(self):
        self.title = "Dynamic Labels - Clean Version"
        self.root = Builder.load_file('dynamic_labels_clean.kv')
        self.add_labels()
        return self.root

    def add_labels(self):
        for i, person in enumerate(self.people, start=1):
            lbl = Label(
                text=f"{i}. {person}",
                font_size=22,
                color=(0, 0, 0, 1),
                size_hint_y=None,
                height=30
            )
            self.root.ids.container.add_widget(lbl)

DynamicLabelsCleanApp().run()
