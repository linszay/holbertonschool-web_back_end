#!/usr/bin/env python3
"""Annotate the function’s params and return values with appropriate types"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """annotate return with appropriate types"""
    return [(i, len(i)) for i in lst]
