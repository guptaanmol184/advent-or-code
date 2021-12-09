# Advent of code Year 2021 Day XX solution
# Author = Anmol Gupta
# Date = December 2021


input = list()
with open("input.txt", "r") as input_file:
    input = input_file.readlines()

# 1 Let us try some map-reduce action
import functools

ans1 = sum(
    map(
        lambda x: functools.reduce(
            lambda a, b: a + 1 if b in [2, 3, 4, 7] else a,
            list(map(len, x.strip().split("|")[1].strip().split(" "))),
            0,
        ),
        input,
    )
)

## pip install pyfunctional
# from functional import seq
#
# a = (
#     seq(input)
#     .map(lambda x: x.split("|"))
#     .map(lambda x: x[1].strip())
#     .map(lambda x: x.split(" "))
#     .map(lambda x: len(x))
#     .flatten()
#     .filter(lambda x: x in [2, 3, 4, 7])
#     .sum()
# )
# print(a)


print("Part One : " + str(ans1))

# 2
"""
Solution to Part 2
"""
print("Part Two : " + str(None))
