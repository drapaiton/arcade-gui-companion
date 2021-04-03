from typing import Callable
from dataclasses import dataclass


def for_every_attribute(method: Callable):
    """
    :param method: to apply once each function
    :type method: Callable
    :return: class with new fields
    :rtype: same as class
    """

    def apply_method(cls: object) -> object:
        """field getter & function apply"""
        for k, v in dataclass(cls).__dataclass_fields__.items():
            v = v.default
            setattr(cls, k, method(v))
        return cls

    return apply_method
