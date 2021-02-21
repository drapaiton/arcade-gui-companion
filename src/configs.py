from os import getenv

from kivy.config import Config

PC_MICROSERVICE_URL = getenv("hey")

Config.write()

if __name__ == "__main__":
    pass
