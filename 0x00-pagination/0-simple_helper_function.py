#!/usr/bin/env python3
"""
A function to calculate the index range for pagination.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the index range for the current page.
    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.
    """
    return (page - 1) * page_size, ((page - 1) * page_size) + page_size
