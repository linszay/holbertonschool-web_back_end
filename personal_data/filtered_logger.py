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
    return re.sub(
        rf'({re.escape(separator)})({"|".join(map(re.
        escape, fields))})({re.escape(separator)})', rf'\1{redaction}\3',
        message
    )
