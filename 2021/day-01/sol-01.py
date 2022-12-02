# Advent of code Year 2021 Day 01 solution
# Author = Anmol Gupta
# Date = December 2021

input = list()
with open("input.txt", 'r') as input_file:
    input = input_file.readlines()

input = [int(num) for num in input]

# 1
ans1 = sum(a < b for a, b in zip(input, input[1:]))
print("Part One : " + str(ans1))

# 2
ans2 = sum(a < b for a, b in zip(input, input[3:]))
print("Part Two : " + str(ans2))
