#!/usr/bin/env python3
"""Testing typ annonatatio."""


from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str | float]:
    """To_kv is a func that Sums list of flaots.

    Args:
        mxd_lst (List[float:int]): list of floats numbers

    Returns:
        float: sum of float numbers
    """
    sqr: float = v*v

    tpl: Tuple = (k, sqr)

    return tpl
