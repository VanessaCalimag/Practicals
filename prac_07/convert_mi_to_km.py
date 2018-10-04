from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
MILES_TO_KILOMETERS = 1.609344


class MilesConverterApp(App):
    def build(self):
        Window.size = (500, 200)
        self.title = "Miles to Kilometers Converter"
        self.root = Builder.load_file('convert_mi_to_km.kv')
        return self.root

    def calculate_mi_to_km(self, value):
        result = value * MILES_TO_KILOMETERS
        self.root.ids.output_label.text = str (result)

    def handle_increment(self):



MilesConverterApp().run()

