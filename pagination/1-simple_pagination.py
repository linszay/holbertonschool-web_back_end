#!/usr/bin/env python3
"""copy index_range from the prev task & server class"""
import csv
from typing import List


def index_range(page, page_size):
    """Return a tuple of start and end indexes"""
    if page < 1 or page_size < 1:
        return (0, 0)

    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = list(reader)
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """takes two integer arguments page and page_size"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start, end = index_range(page, page_size)

        return [] if start >= len(dataset) else dataset[start:end]
