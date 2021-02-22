from os import pardir
from os.path import abspath
from os.path import dirname
from os.path import join

from src.utils import dataclass_with_prefix

_SCRIPT_PATH = dirname(abspath(__file__))
_STATIC_FOLDER = join(_SCRIPT_PATH, pardir, "static")


_SOUNDS_FOLDER = join(_STATIC_FOLDER, "sounds")
_IMAGES_FOLDER = join(_STATIC_FOLDER, "images")
_VIDEOS_FOLDER = join(_STATIC_FOLDER, "videos")


@dataclass_with_prefix(_IMAGES_FOLDER)
class SOUNDS:
    pass


@dataclass_with_prefix(_IMAGES_FOLDER)
class IMAGES:
    pass


@dataclass_with_prefix(_VIDEOS_FOLDER)
class VIDEOS:
    FAIRPLAY: str = "fairplay.mp4"
