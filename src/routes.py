from os import pardir
from os.path import abspath
from os.path import dirname
from os.path import join

from src.utils import dataclass_join_attrs

_SCRIPT_PATH = dirname(abspath(__file__))
_ROOT_FOLDER = join(_SCRIPT_PATH, pardir)
_STATIC_FOLDER = join(_ROOT_FOLDER, "static")
_SOUNDS_FOLDER = join(_STATIC_FOLDER, "sounds")
_IMAGES_FOLDER = join(_STATIC_FOLDER, "images")
_VIDEOS_FOLDER = join(_STATIC_FOLDER, "videos")

LAYOUT_FOLDER = join(_ROOT_FOLDER, "layouts")


@dataclass_join_attrs(_IMAGES_FOLDER)
class SOUNDS:
    pass


@dataclass_join_attrs(_IMAGES_FOLDER)
class IMAGES:
    pass


@dataclass_join_attrs(_VIDEOS_FOLDER)
class VIDEOS:
    FAIRPLAY: str = "fairplay.mp4"
