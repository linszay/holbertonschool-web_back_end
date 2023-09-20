#!/usr/bin/env python3
"""filter_datum returns log message obfuscated(type annotated)"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """use regex to replace occurences of certain field values"""
    """select separator char and its surrounding parentheses"""
    """"|".join(map(re.escape, creates regex pattern to match fields and joins them"""
    """capture separator character after field"""
    """replace 1st capture group with 3rd capture group"""
    ree = re.escape
    sep = separator
    red = redaction
    return re.sub(
        rf'({ree(sep)})({"|".join(map(ree, fields))})({ree(sep)})', rf'\1{red}\3',
        message
    )
