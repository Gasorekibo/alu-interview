#!/usr/bin/python3
"""
    Creating a function that will return minimun operation
"""


def minOperations(n):
    """
        this function will return the minimun number of operation
    """
    if n == 1:
        return 0
    nbr_operations = 0
    copy_count = 1
    paste_count = 0

    while copy_count < n:
        if n % copy_count == 0:
            paste_count = copy_count
            nbr_operations += 1
        copy_count += paste_count
        nbr_operations += 1

    return nbr_operations
