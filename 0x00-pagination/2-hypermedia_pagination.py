#!/usr/bin/env python3
""" Pagination """

import math
from typing import Dict
Server = __import__('1-simple_pagination').Server


def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
    """ Get hyper information for a given page number """
    data = self.get_page(page, page_size)
    total_pages = math.ceil(len(self.dataset()) / page_size)
    prev_page = page - 1
    next_page = page + 1

    result = {
        'page_size': len(data),
        'page': page,
        'data': data,
        'next_page': next_page if next_page <= total_pages > 0 else None,
        'prev_page': prev_page if prev_page else None,
        'total_pages': total_pages
    }

    return result


Server.get_hyper = get_hyper
