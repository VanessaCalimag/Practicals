from kivy.app import App
from kivy.lang import Builder

MILES_TO_KILOMETERS = 1.609344

class MilesConverterApp(App):
    def build(self):
        self.title = "Miles to Kilometers Converter"
        self.root = Builder.load_file('convert_mi_to_km.kv')
        return self.root

