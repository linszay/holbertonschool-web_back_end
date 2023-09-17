#!/usr/bin/env python3
"""index_range takes two int args page and page_size"""


def index_range(page, page_size):
    """Return a tuple of start and end indexes"""
    if page < 1 or page_size < 1:
        return (0, 0)

    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
