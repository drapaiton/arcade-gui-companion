from kivy.app import App

from src.routes import LAYOUT_FOLDER
from src.widgets.full import OverridableLayout


class MainApp(App):
    kv_directory = LAYOUT_FOLDER
    title = "MainApp"

    def build(self):
        return OverridableLayout()


if __name__ == "__main__":
    pass
