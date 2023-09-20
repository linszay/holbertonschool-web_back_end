#!/usr/bin/env python3
"""filter_datum returns log message obfuscated(type annotated)"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """use regex to replace occurences of certain field values"""
    return re.sub(
        rf'({re.escape(separator)})({"|".join(map(re.
        escape, fields))})({re.escape(separator)})', rf'\1{redaction}\3',
        message
    )
