
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


CONVERSION_FACTOR = 1.60934


class DistanceConverterApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('m_to_km.kv')
        return self.root

    def handle_increment(self, increment):
        try:
            value = float(self.root.ids.input_number.text)
        except ValueError:
            value = 0.0
        result = value + increment
        converted_value = value * CONVERSION_FACTOR
        self.root.ids.input_number.text = str(result)
        self.root.ids.output_label.text = str(converted_value)

    # def handle_conversion(self):
    #     try:
    #         value = float(self.root.ids.input_number.text)
    #     except ValueError:
    #         value = 0.0
    #     result = value * CONVERSION_FACTOR
    #     self.root.ids.output_label.text = str(result)


DistanceConverterApp().run()
