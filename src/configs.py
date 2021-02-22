from os import getenv
from kivy.config import Config

PC_MICROSERVICE_URL = getenv("PC_MICROSERVICE_URL")
PRODUCTION = getenv("PRODUCTION", default=False)

Config.set("graphics", "resizable", False)
Config.set("graphics", "width", "1280")
Config.set("graphics", "height", "400")

if PRODUCTION:
    Config.set("graphics", "fullscreen", True)
    Config.set("graphics", "borderless", 1)
    Config.set("graphics", "show_cursor", 0)
else:
    Config.set("graphics", "fullscreen", False)
    Config.set("graphics", "borderless", 0)
    Config.set("graphics", "show_cursor", 1)


if __name__ == "__main__":
    pass
