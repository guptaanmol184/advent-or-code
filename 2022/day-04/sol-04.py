# Advent of code Year 2022 Day 04 solution
# Author = Anmol Gupta
# Date = December 2022

from typing import Tuple

input = list()
with open("input.txt", 'r') as input_file:
    input = input_file.readlines()
    input = [line.strip().split(',') for line in input]
    input = [(tuple(map(int, first.split('-'))),
              tuple(map(int, second.split('-'))))
              for first, second
              in input]

# 1
"""
Solution to Part 1
"""


def does_fully_overlap(input: Tuple[Tuple[int, int], Tuple[int, int]]) -> bool:

    first, second = input
    a1, b1 = first
    a2, b2 = second

    return (a1 <= a2 and b2 <= b1) or (a2 <= a1 and b1 <= b2)

ans = sum(map(does_fully_overlap, input))
print("Part One : " + str(ans))

# 2
"""
Solution to Part 2
"""

def does_overlap(input: Tuple[Tuple[int, int], Tuple[int, int]]) -> bool:

    first, second = input
    a1, b1 = first
    a2, b2 = second

    return not ((a1 < a2 and b1 < a2) or (a2 < a1 and b2 < a1))

ans2 = sum(map(does_overlap, input))
print("Part Two : " + str(ans2))
