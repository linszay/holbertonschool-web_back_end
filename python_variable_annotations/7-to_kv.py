#!/usr/bin/env python3
"""type-annotated func to_kv takes a string k & an int OR float v as args"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """returns a tuple - first element is k and second is v"""
    return (k, v**2)
