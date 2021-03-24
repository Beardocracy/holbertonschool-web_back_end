#!/usr/bin/env python3
'''
Hypermedia pagination
'''
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Returns the index numbers of a range in a tuple
    '''
    return ((page - 1) * page_size, page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' Checks input and returns list of rows from dataset
        '''
        assert type(page) == int
        assert page > 0
        assert type(page_size) == int
        assert page_size > 0
        beg, end = index_range(page, page_size)
        return self.dataset()[beg:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' Returns a dictionary of data
        '''
        total_pages = math.ceil(len(self.dataset()) / page_size)
        data = self.get_page(page, page_size)
        page_size = page_size if page < total_pages else 0
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
