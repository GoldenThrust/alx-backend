#!/usr/bin/env python3
""" Pagination """


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """ Returns a tuple of (start index, end index) of a page"""
    number_of_page = page_size * page
    return (number_of_page - page_size, number_of_page)
