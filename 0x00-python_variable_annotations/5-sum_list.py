#!/usr/bin/env python3
"""Testing typ annonatatio."""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum_list is a func that Sums list of flaots.

    Args:
        input_list (List[float]): list of floats numbers

    Returns:
        float: sum of float numbers
    """
    list_sum: float = 0

    for num in input_list:
        list_sum += num

    return list_sum
