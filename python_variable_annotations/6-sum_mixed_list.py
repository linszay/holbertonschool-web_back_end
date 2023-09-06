#!/usr/bin/env python3
"""type-annotated function sum_mixed_list takes a list mxd_lst of ints and floats"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """returns their sum as a float"""
    return sum(mxd_lst)
