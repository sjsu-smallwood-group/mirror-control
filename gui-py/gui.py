from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


class SliderApp(App):
    def build(self):
        layout = FloatLayout()
        vslider = Slider(
            orientation="vertical",
            pos_hint={"x": 0.45, "y": 0.2},
            size_hint=(0.1, 0.6),
            value=100,
        )
        hslider = Slider(
            pos_hint={"x": 0.2, "y": 0.45}, size_hint=(0.6, 0.1), value=100
        )

        vslider_label = Label(
            text="Vertical Slider",
            pos_hint={"x": 0.4, "y": 0.85},
            size_hint=(0.2, 0.05),
        )
        hslider_label = Label(
            text="Horizontal Slider",
            pos_hint={"x": 0.4, "y": 0.15},
            size_hint=(0.2, 0.05),
        )

        vslider_input_label = Label(
            text="Vertical mirror position:",
            pos_hint={"x": 0.65, "y": 0.95},
            size_hint=(0.2, 0.05),
        )
        hslider_input_label = Label(
            text="Horizontal mirror position:",
            pos_hint={"x": 0.6, "y": 0.9},
            size_hint=(0.25, 0.05),
        )

        vslider_input = TextInput(
            text="100",
            pos_hint={"x": 0.8, "y": 0.95},
            size_hint=(0.2, 0.05),
            input_filter="int",
        )
        hslider_input = TextInput(
            text="100",
            pos_hint={"x": 0.8, "y": 0.9},
            size_hint=(0.2, 0.05),
            input_filter="int",
        )

        button = Button(
            text="Send to Arduino",
            pos_hint={"x": 0.35, "y": 0.05},
            size_hint=(0.3, 0.1),
        )

        def on_vslider_value(instance, value):
            vslider_input.text = str(int(value))

        def on_hslider_value(instance, value):
            hslider_input.text = str(int(value))

        vslider.bind(value=on_vslider_value)
        hslider.bind(value=on_hslider_value)

        def on_vslider_input(instance, value):
            try:
                vslider.value = int(value)
            except ValueError:
                pass

        def on_hslider_input(instance, value):
            try:
                hslider.value = int(value)
            except ValueError:
                pass

        vslider_input.bind(text=on_vslider_input)
        hslider_input.bind(text=on_hslider_input)

        layout.add_widget(vslider)
        layout.add_widget(hslider)
        layout.add_widget(button)
        layout.add_widget(vslider_label)
        layout.add_widget(hslider_label)
        layout.add_widget(vslider_input_label)
        layout.add_widget(hslider_input_label)
        layout.add_widget(vslider_input)
        layout.add_widget(hslider_input)
        return layout

    def on_start(self):
        self.root_window.title = "Control mirror movement using Arduino"


if __name__ == "__main__":
    SliderApp().run()
