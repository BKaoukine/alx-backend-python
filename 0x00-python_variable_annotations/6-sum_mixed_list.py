#!/usr/bin/env python3
"""Testing typ annonatatio."""


from typing import List


def sum_mixed_list(mxd_lst: List[float | int]) -> float:
    """Sum_mixed_list is a func that Sums list of flaots.

    Args:
        mxd_lst (List[float:int]): list of floats numbers

    Returns:
        float: sum of float numbers
    """
    list_sum: float = 0

    for num in mxd_lst:
        list_sum += num

    return list_sum
