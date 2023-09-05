#!/usr/bin/env python3
import typing
"""type-annotated function sum_list which input_list of floats as arg"""
"""returns their sum as a float"""
"""uses typing library for list type annotation"""


def sum_list(input_list: typing.List[float]) -> float:
    """sum_list returns input_list sum as a float"""
    return sum(input_list)
