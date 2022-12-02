# Advent of code Year 2021 Day 21 solution
# Author = Anmol Gupta
# Date = December 2021

input = list()
with open("input.txt", "r") as input_file:
    input = input_file.readlines()

pos1, pos2 = [int(line.strip().split(": ")[1]) for line in input]


def play_part_1(pos1, pos2, score1=0, score2=0, i=0):
    if score2 >= 1000:
        return score1 * i

    pos1 = (pos1 + 3 * i + 6) % 10 or 10
    return play_part_1(pos2, pos1, score2, score1 + pos1, i + 3)


from functools import cache
from collections import Counter
import itertools

dirac_die_rolls = Counter(
    sum(r) for r in itertools.product([1, 2, 3], repeat=3)
).most_common()


@cache
def play_part_2(pos1, pos2, score1=0, score2=0):
    if score2 >= 21:
        return 0, 1

    wins1, wins2 = 0, 0
    for move, count in dirac_die_rolls:
        pos1_ = (pos1 + move) % 10 or 10
        w2, w1 = play_part_2(pos2, pos1_, score2, score1 + pos1_)
        wins1, wins2 = wins1 + count * w1, wins2 + count * w2
    return wins1, wins2


# 1
"""
Solution to Part 1
"""
print("Part One : " + str(play_part_1(pos1, pos2)))

# 2
"""
Solution to Part 2
"""
print("Part Two : " + str(max(play_part_2(pos1, pos2))))
