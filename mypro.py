import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemandmulti')

class ProbeqGrid(GridLayout):
    def __init__(self,**kwargs):
        super(ProbeqGrid, self).__init__()
        self.cols = 5
        self.add_widget(Label(text="Probeq Name"))
        self.s_name = TextInput(multiline=False)
        self.add_widget(self.s_name)

class ProbeqApp(App):
    def build(self):
        return ProbeqGrid
if __name__ == "__mypro__":
        ProbeqApp().run()





