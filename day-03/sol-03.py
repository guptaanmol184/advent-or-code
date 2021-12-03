# Advent of code Year 2021 Day XX solution
# Author = Anmol Gupta
# Date = December 2021

from typing import Counter
import pandas as pd

input = list()
with open("input.txt", 'r') as input_file:
    input = input_file.readlines()

input = [list(line.strip()) for line in input]

# 1
# Using pandas for finding the mode of each column
# numpy could might have been simpler...
df = pd.DataFrame(input)

gamma_rate_str_binary = ''.join(list(df.mode().iloc[0]))
gamma_rate_int_decimal = int(gamma_rate_str_binary, 2)
epsilon_rate_int_decimal = gamma_rate_int_decimal ^ 0xFFF

# print(gamma_rate_int_decimal)
# print(bin(gamma_rate_int_decimal))
# print(epsilon_rate_int_decimal)
# print(bin(epsilon_rate_int_decimal))

print("Part One : " + str(gamma_rate_int_decimal * epsilon_rate_int_decimal))

# 2
input = list()
with open("input.txt", 'r') as input_file:
    input = input_file.readlines()
input = [list(line.strip()) for line in input]

for i in range(12):
    common = Counter([number[i] for number in input])

    if common['0'] > common['1']:
        input = [number for number in input if number[i] == '0']
    else:
        input = [number for number in input if number[i] == '1']

    oxygen_generator_rating_bin_str = ''.join(input[0])


input = list()
with open("input.txt", 'r') as input_file:
    input = input_file.readlines()
input = [list(line.strip()) for line in input]

for i in range(12):
    common = Counter(number[i] for number in input)

    if common['0'] > common['1']:
        input = [number for number in input if number[i] == '1']
    else:
        input = [number for number in input if number[i] == '0']

    if input:
        co2_scrubber_rating_bin_str = ''.join(input[0])

print("Part Two : " + str(int(oxygen_generator_rating_bin_str, 2)
      * int(co2_scrubber_rating_bin_str, 2)))
