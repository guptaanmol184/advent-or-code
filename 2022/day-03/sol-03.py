# Advent of code Year 2022 Day 03 solution
# Author = Anmol Gupta
# Date = December 2022

from typing import List

input = list()
with open("input.txt", 'r') as input_file:
    input = input_file.readlines()
    rucksacks: List[str] = [line.strip() for line in input]

# 1
"""
Solution to Part 1
"""


def get_shared_item_priority(item_list: str):
    mid: int = len(item_list)//2
    first_compartment: str = item_list[:mid]
    second_compartment: str = item_list[mid:]
    shared_item_set: set = set(first_compartment) \
        .intersection(set(second_compartment))

    # ensure single shared item
    assert len(shared_item_set) == 1

    shared_item: str = list(shared_item_set)[0]
    priority: int
    if shared_item.isupper():
        priority = ord(shared_item) - ord('A') + 27
    else:
        priority = ord(shared_item) - ord('a') + 1

    return priority

priority_sum = sum(map(get_shared_item_priority, rucksacks))
print("Part One : " + str(priority_sum))

# 2
"""
Solution to Part 2
"""
def get_shared_item_priority_in_elve_group(rucksack_list: List[str]):
    assert len(rucksack_list) == 3
    shared_item_set = set.intersection(*[set(rucksack) for rucksack in rucksack_list])

    # ensure single shared item
    assert len(shared_item_set) == 1

    shared_item: str = list(shared_item_set)[0]
    priority: int
    if shared_item.isupper():
        priority = ord(shared_item) - ord('A') + 27
    else:
        priority = ord(shared_item) - ord('a') + 1

    return priority

rucksacks_by_elve_groups = [rucksacks[i: i + 3] for i in range(0, len(rucksacks), 3)]
priority_sum = sum(map(get_shared_item_priority_in_elve_group, rucksacks_by_elve_groups))

print("Part Two : " + str(priority_sum))
