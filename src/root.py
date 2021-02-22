from enum import Enum

from kivy.properties import ColorProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.video import Video
from kivy.uix.widget import Widget

from src.routes import VIDEOS


class RootMenu(FloatLayout):
    """"""

    def __init__(self):
        super(RootMenu, self).__init__()
        self.add_widget(OnlyPlayer())


class PrincipalButtons(BoxLayout):
    """"""

    def boton1(self):
        print("hola")


class OnlyPlayer(Video):
    def __init__(self, **kwargs):
        super(OnlyPlayer, self).__init__(
            state="play", keep_ratio=False, allow_stretch=True
        )
        self.source = VIDEOS.FAIRPLAY
        for k, v in kwargs.items():
            setattr(self, k, v)

    def hide_player(self):
        self.color = [1, 1, 1, 0]

    def on_state(self, instance, value):
        if not self._video:
            return
        if value == "play":
            if self.eos:
                self._video.stop()
                self._video.position = 0.0
            self.eos = False
            self._video.play()
        elif value == "pause":
            self.hide_player()
            self._video.pause()
        else:
            self.hide_player()
            self._video.stop()
            self._video.position = 0


class MainApp(App):
    kv_directory = "../layouts"
    title = "MainApp"

    def build(self):
        return RootMenu()


if __name__ == "__main__":
    pass
