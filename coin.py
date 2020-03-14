import itertools
from typing import List


def make_change(total: int, coins: List):
    if total == 0 or len(coins) == 0:
        return 0

    max_number_of_elements = int(total / min(coins))
    combinations = []

    for length in range(max_number_of_elements):
        for combination in list(itertools.combinations_with_replacement(coins, length + 1)):
            if sum(combination) == total:
                combinations.append(combination)

    return len(combinations)

