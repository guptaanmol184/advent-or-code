# Advent of code Year 2021 Day XX solution
# Author = Anmol Gupta
# Date = December 2021

import heapq

input = list()
with open("input.txt", 'r') as input_file:
    input = input_file.readlines()
    input = [number.strip() for number in input]


def get_cal_sum(input):
    input.append('')
    s = 0
    for calories in input:
        if calories == '':
            yield s
            s = 0
        else:
            s += int(calories)


# 1
"""
Solution to Part 1
"""
maxx_cal = max(get_cal_sum(input))

print("Part One : " + str(maxx_cal))

# 2
"""
Solution to Part 2
"""
ans = sum(heapq.nlargest(3, get_cal_sum(input)))
print("Part Two : " + str(ans))
