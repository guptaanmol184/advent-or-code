# Advent of code Year 2021 Day 13 solution
# Author = Anmol Gupta
# Date = December 2021

import pprint

input = list()
with open("input.txt", "r") as input_file:
    input = input_file.readlines()

dots_coordinates = set()
fold_instructions = []

fold_instructions_start = False
for line in input:
    if line == "\n":
        fold_instructions_start = True
        continue

    if fold_instructions_start:
        instruction, value = line.strip().split("=")
        fold_instructions.append((instruction[-1], int(value)))
    else:
        x, y = list(map(int, line.strip().split(",")))
        dots_coordinates.add((x, y))

# 1
"""
Solution to Part 1
"""
# Perform the first fold and count the number of points in the sheet

# Performs the fold instruction and modifies the dots_coordinates in place
def perform_fold(instruction, dots_coordinates):
    updated_dots_coordinates = set()
    axis, value = instruction
    if axis == "x":
        for x, y in dots_coordinates:
            if x > value:
                dist = x - value
                if dist < 0:
                    print("negative fold")
                updated_dots_coordinates.add((value - dist, y))
            else:
                updated_dots_coordinates.add((x, y))
    else:
        for x, y in dots_coordinates:
            if y > value:
                dist = y - value
                if dist < 0:
                    print("negative fold")
                updated_dots_coordinates.add((x, value - dist))
            else:
                updated_dots_coordinates.add((x, y))
    return updated_dots_coordinates


points_after_first_fold = 0
for idx, fold_instruction in enumerate(fold_instructions):
    dots_coordinates = perform_fold(fold_instruction, dots_coordinates)
    if idx == 0:
        points_after_first_fold = len(dots_coordinates)

print("Part One : " + str(points_after_first_fold))

# 2
# Print the paper after completing all the folds
max_x = max_y = 0

for point in dots_coordinates:
    x, y = point

    max_x = x if x > max_x else max_x
    max_y = y if y > max_y else max_y

for i in range(max_y + 1):
    print()
    for j in range(max_x + 1):
        point = (j, i)
        if point in dots_coordinates:
            print("#", end="")
        else:
            print(" ", end="")
print()

print("Part Two : " + "EPUELPBR")
