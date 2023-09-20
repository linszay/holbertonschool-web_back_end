#!/usr/bin/env python3
"""filter_datum returns log message obfuscated(type annotated)"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, 
                 message: str, separator: str) -> str:
    """use regex to replace occurences of certain field values"""
    for field in fields:
        """regex syntax to match current position, start of str, empty str"""
        message = re.sub(fr'(?<=\{separator}|^){re.escape(field)}\b[^{separator}]*', redaction, message)

    return message
