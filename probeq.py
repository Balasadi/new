import kivy
from kivy.app import App
from kivy.uix.label import Label


class ProbeqApp(App):

    def build(self):
        return Label(text="This is ProbeQ!!!")


if __name__ == "__probeq__":
    ProbeqApp().run()