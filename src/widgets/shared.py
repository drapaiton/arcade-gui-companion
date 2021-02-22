from kivy.uix.boxlayout import BoxLayout

from kivy.uix.floatlayout import FloatLayout


class OverridableLayout(FloatLayout):
    """"""

    def __init__(self):
        super(OverridableLayout, self).__init__()
        # self.add_widget(OnlyPlayer())


class ButtonList(BoxLayout):
    """"""

    def boton1(self):
        print("hola")
