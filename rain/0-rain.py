#!/usr/bin/python3
def rain(walls):
    """
    Calculate the amount of water retained between walls.

    Args:
        walls (List[int]): A list of non-negative integers representing the heights of walls.

    Returns:
        int: The total amount of water retained.

    Raises:
        None

    Examples:
        >>> rain([3, 0, 2, 0, 4])
        5
    """
    if not walls:
        return 0

    left = 0
    right = len(walls) - 1
    left_max = 0
    right_max = 0
    total_water = 0

    while left < right:
        if walls[left] <= walls[right]:
            if walls[left] > left_max:
                left_max = walls[left]
            else:
                total_water += left_max - walls[left]
            left += 1
        else:
            if walls[right] > right_max:
                right_max = walls[right]
            else:
                total_water += right_max - walls[right]
            right -= 1

    return total_water
