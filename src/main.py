from configs import *
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.video import Video


class VideoWindow(App):
    def build(self):
        video = Video(
            source="video.mp4",
            state="play",
            eos="loop",
            options={"allow_stretch": True},
        )
        # video.allow_stretch = True
        return video


if __name__ == "__main__":
    PC_MICROSERVICE_URL = ""
    window = VideoWindow()
    window.run()
