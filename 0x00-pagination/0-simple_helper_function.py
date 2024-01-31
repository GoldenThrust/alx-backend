#!/usr/bin/env python3
""" Pagination """


def index_range(page: int, page_size: int) -> tuple:
    """ Returns a tuple of (start index, end index) of a page"""
    end_index = page_size * page
    return (end_index - page_size, end_index)

