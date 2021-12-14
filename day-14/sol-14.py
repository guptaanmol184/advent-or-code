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
    insertion_rules[lhs] = rhs

c = Counter(template)

for i in range(10):
    num_inserts = 0
    new_template = template[:]
    for i in range(len(template) - 1):
        window = template[i : i + 2]
        try:
            to_insert = insertion_rules["".join(window)]
            new_template = (
                new_template[: i + 1 + num_inserts]
                + [to_insert]
                + new_template[i + 1 + num_inserts :]
            )
            num_inserts += 1
            c[to_insert] += 1
        except KeyError:
            continue
    template = new_template

ans1 = max(c.values()) - min(c.values())

# 1
"""
Solution to Part 1
"""
print("Part One : " + str(ans1))

# 2
"""
Solution to Part 2
"""
print("Part Two : " + str(None))
