#!/usr/bin/env python3
import typing
"""type-annotated function sum_list which takes a list input_list of floats as argument"""
"""returns their sum as a float"""


def sum_list(input_list: typing.List[float]) -> float:
    """returns their sum as a float"""
    return sum(input_list)
