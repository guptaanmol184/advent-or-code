# Advent of code Year 2021 Day 14 solution
# Author = Anmol Gupta
# Date = December 2021

from collections import Counter

input = list()
with open("input.txt", "r") as input_file:
    input = input_file.readlines()

template = list(input[0].strip())
insertion_rules = {}
for line in input[2:]:
    lhs, rhs = line.strip().split(" -> ")
    insertion_rules[(lhs[0], lhs[1])] = rhs


letter_counter = Counter(template)

polymer_counter = Counter()
for i in range(len(template) - 1):
    key = (template[i], template[i + 1])
    polymer_counter[key] += 1

for i in range(40):
    udpated_polymer_counter = Counter()
    for key, val in polymer_counter.items():
        try:
            c = insertion_rules[key]
            udpated_polymer_counter[(key[0], c)] += val
            udpated_polymer_counter[(c, key[1])] += val
            letter_counter[c] += val
        except:
            udpated_polymer_counter[key] += val
    polymer_counter = udpated_polymer_counter
    if i == 9:
        ans1 = max(letter_counter.values()) - min(letter_counter.values())
    if i == 39:
        ans2 = max(letter_counter.values()) - min(letter_counter.values())


# 1
"""
Solution to Part 1
"""
print("Part One : " + str(ans1))

# 2
"""
Solution to Part 2
"""
print("Part Two : " + str(ans2))
