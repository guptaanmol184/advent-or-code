# Advent of code Year 2022 Day 06 solution
# Author = Anmol Gupta
# Date = December 2022

input = list()
with open("input.txt", 'r') as input_file:
    input = input_file.readlines()

signal = input[0].strip()
# 1
"""
Solution to Part 1
"""
def check_if_start_of_marker(input, position, length):
    inspection_string = input[position-(length-1): position+1]
    return len(set(inspection_string)) == length

index = -1
for i in range(3, len(signal)):
    if check_if_start_of_marker(signal, i, 4):
        index = i
        break

ans = index+1
print("Part One : " + str(ans))

# 2
"""
Solution to Part 2
"""
index = -1
for i in range(13, len(signal)):
    if check_if_start_of_marker(signal, i, 14):
        index = i
        break

ans = index+1
print("Part Two : " + str(ans))
