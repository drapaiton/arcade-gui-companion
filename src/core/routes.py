from os import pardir
from os.path import abspath
from os.path import dirname
from os.path import join

from src.core.decorators import for_every_attribute

_SCRIPT_PATH = dirname(abspath(__file__))
_ROOT_FOLDER = join(_SCRIPT_PATH, pardir)
STATIC_FOLDER = join(_ROOT_FOLDER, "static")

_SOUNDS_FOLDER = join(STATIC_FOLDER, "sounds")
_IMAGES_FOLDER = join(STATIC_FOLDER, "images")
_VIDEOS_FOLDER = join(STATIC_FOLDER, "videos")

LAYOUT_FOLDER = join(_ROOT_FOLDER, "layouts")


@for_every_attribute(lambda x: join(_SOUNDS_FOLDER, x))
class SOUNDS:
    """every member is a resource path"""

    pass


@for_every_attribute(lambda x: join(_VIDEOS_FOLDER, x))
class IMAGES:
    """every member is a resource path"""

    pass


@for_every_attribute(lambda x: join(_IMAGES_FOLDER, x))
class VIDEOS:
    """every member is a resource path"""

    FAIRPLAY = "fairplay.mp4"
