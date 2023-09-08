#!/usr/bin/env python3
"""Annotate the function’s params and return values with appropriate types"""
import typing


seq = typing.Sequence
tup = typing.Tuple
def element_length(lst: typing.Iterable[seq]) -> typing.List[tup[seq, int]]:
    """annotate return with appropriate types"""
    return [(i, len(i)) for i in lst]
