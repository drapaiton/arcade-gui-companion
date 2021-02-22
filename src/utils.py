from dataclasses import dataclass
from os.path import join


def dataclass_join_attrs(prefix: str):
    """creates a dataclass then adds prefix to every attribute"""

    def decorate(cls):
        cls = dataclass(cls)
        for k, v in cls.__dataclass_fields__.items():
            new_value = join(prefix, v.default)
            setattr(cls, k, new_value)
            cls.__dataclass_fields__[k].default = new_value
        return cls

    return decorate
