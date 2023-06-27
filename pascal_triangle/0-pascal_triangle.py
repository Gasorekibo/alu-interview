#!/usr/bin/python3
"""
    pascal triangle.py
"""


def pascal_triangle(n):
    """
    Returns right angled triangle.
    """
    if n == 0:
        return []
    return [[1]] + pascal_triangle(n - 1)
