# Advent of code Year 2021 Day 07 solution
# Author = Anmol Gupta
# Date = December 2021

from collections import Counter
import sys

input = list()
with open("input.txt", "r") as input_file:
    input = input_file.readlines()

horizontal_positions = [int(position) for position in input[0].strip().split(",")]

# 1
# Find the cheapest position for moving all the crabs
c = Counter(horizontal_positions)
mini = sys.maxsize
for move_position in c.keys():
    fuel_cost = 0
    for postion, count in c.items():
        fuel_cost += abs(postion - move_position) * count
    mini = fuel_cost if fuel_cost < mini else mini

print("Part One : " + str(mini))

# 2
# Find the cheapest position for moving all the crabs, with the updated fueld cumsuption function
c = Counter(horizontal_positions)
mini = sys.maxsize

crab_positions = c.keys()
start_position = min(crab_positions)
end_position = max(crab_positions)

for move_position in range(start_position, end_position + 1):
    total_fuel_cost = 0
    for postion, count in c.items():
        move_dist = abs(postion - move_position)
        fuel_cost = (move_dist * (move_dist + 1)) // 2
        total_fuel_cost += fuel_cost * count
    mini = total_fuel_cost if total_fuel_cost < mini else mini
print("Part Two : " + str(mini))
