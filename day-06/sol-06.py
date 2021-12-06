# Advent of code Year 2021 Day XX solution
# Author = Anmol Gupta
# Date = December 2021

from collections import Counter

input = list()
with open("input.txt", "r") as input_file:
    input = input_file.readlines()

fish_ages = [int(age) for age in input[0].strip().split(",")]

# 1
"""
Solution to Part 1
"""

fish_age_counter: Counter = Counter(fish_ages)

for i in range(80):
    age_0_fishes = fish_age_counter[0]
    for i in range(8):
        fish_age_counter[i] = fish_age_counter[i + 1]
    fish_age_counter[8] = age_0_fishes
    fish_age_counter[6] += age_0_fishes

print("Part One : " + str(sum(fish_age_counter.values())))

# 2
"""
Solution to Part 2
"""

fish_age_counter: Counter = Counter(fish_ages)

for i in range(256):
    age_0_fishes = fish_age_counter[0]
    for i in range(8):
        fish_age_counter[i] = fish_age_counter[i + 1]
    fish_age_counter[8] = age_0_fishes
    fish_age_counter[6] += age_0_fishes

print("Part Two : " + str(sum(fish_age_counter.values())))
