#!/usr/bin/env python3
"""type-annotated func make_multiplier takes a float multiplier as arg"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def multiplication(num: float) -> float:
        return num * multiplier
    return (multiplication)
