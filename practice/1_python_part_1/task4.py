"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]
    >>> calculate_power_with_difference([1, 2, 3, 4])
    [1, 4, 7, 12]
    >>> calculate_power_with_difference([])
    []
"""
from typing import List


def calculate_power_with_difference(ints: List[int]) -> List[int]:
    powers = []

    if ints:
        powers.append(ints[0]**2)

    for i in range(1, len(ints)):
        powers.append(ints[i]**2 - (powers[i-1] - ints[i-1]))

    return powers


if __name__ == "__main__":
    import doctest
    doctest.testmod()
