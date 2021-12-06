# Advent of code Year 2021 Day 02 solution
# Author = Anmol Gupta
# Date = December 2021

input = list()
with open("input.txt", "r") as input_file:
    input = input_file.readlines()


def get_command(line):
    splitInput = line.strip().split()
    return (splitInput[0], int(splitInput[1]))


input_commands = [get_command(line) for line in input]

# 1
horizontal_position = 0
depth = 0

for action, magnitude in input_commands:
    if action == "forward":
        horizontal_position += magnitude
    elif action == "up":
        depth -= magnitude
    elif action == "down":
        depth += magnitude

print("Part One : " + str(horizontal_position * depth))

# 2
horizontal_position = 0
depth = 0
aim = 0

for action, magnitude in input_commands:
    if action == "forward":
        horizontal_position += magnitude
        depth += aim * magnitude
    elif action == "up":
        aim -= magnitude
    elif action == "down":
        aim += magnitude

print("Part Two : " + str(horizontal_position * depth))
