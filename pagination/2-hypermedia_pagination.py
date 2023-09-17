#!/usr/bin/env python3
"""copy code from the prev task"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """Return a tuple of start and end indexes"""
    if page < 1 or page_size < 1:
        return (0, 0)

    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """copied server class per instructions"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """server constructor"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """dataset"""
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
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """get paginated data using get_page"""
        data = self.get_page(page, page_size)

        """find total number of pages"""
        total_pages = math.ceil(len(self.dataset()) / page_size)

        """get next and prev page numbers"""
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        """return the new dict"""
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
