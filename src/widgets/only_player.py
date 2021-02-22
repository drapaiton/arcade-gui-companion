from kivy.uix.video import Video

from src.routes import VIDEOS


class OnlyPlayer(Video):
    VIDEOS = VIDEOS

    def __init__(self, **kwargs):
        super(OnlyPlayer, self).__init__()
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def visible(self):
        return bool(self.color[-1])

    @visible.setter
    def visible(self, enable: bool):
        self.color[-1] = int(enable)

    def on_state(self, instance, value):
        if not self._video:
            return
        if value == "play":
            self.visible = True
            if self.eos:
                self._video.stop()
                self._video.position = 0.0
            self.eos = False
            self._video.play()
        elif value == "pause":
            self.visible = False
            self._video.pause()
        else:
            self.visible = False
            self._video.stop()
            self._video.position = 0
