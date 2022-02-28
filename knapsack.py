#! /usr/bin/env python3
"""This module solves Exercism's knapsack exercise."""
from numbers import Real
from typing import Dict, Sequence
def maximum_value(maximum_weight: Real, items: Sequence[Dict[str, Real]]):
    """
    Calculate the maximal value for a classic 0/1-knapsack problem.
 
    :param maximum_weight: The maximum combined weight of the selected
        items.
    :param items: A sequence of items, where each item has a "weight"
        and "value".
    :return: The maximal value of items whose combined weight is smaller
        than `maximum_weight`
    """
    # dp[w] holds the maximum value of items with a combined weight of up to w
    dp = [0] * (maximum_weight + 1)
    for item in items:
        weight, value = item['weight'], item['value']
        for max_weight in range(maximum_weight, weight - 1, -1):
            max_value_without_item = dp[max_weight]
            max_value_with_item = value + dp[max_weight - weight]
            dp[max_weight] = max(max_value_without_item, max_value_with_item)
    return dp[maximum_weight]