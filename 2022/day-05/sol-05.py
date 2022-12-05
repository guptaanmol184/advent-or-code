# Advent of code Year 2022 Day XX solution
# Author = Anmol Gupta
# Date = December 2022

from typing import List
import copy

input = list()
with open("input.txt", 'r') as input_file:
    input = input_file.readlines()

# parse input
input = [line.strip() for line in input]
split_index = input.index("")
stack_diagram, operations = input[:split_index], input[split_index+1:]

# parse stacks
num_stacks = int(stack_diagram[-1].split()[-1])
del stack_diagram[-1]
stacks = [[] for _ in range(num_stacks)]
for line in reversed(stack_diagram):
    line = line + " "
    #print(line)
    for i in range(len(line)//4):
        char = line[4*i + 1:4*i + 2]
        if char != ' ':
            stacks[i].append(char)

#print(stacks)

# parse operations
operations = [word.split() for word in operations]
operations = [[word for word in line if word.isdigit()] for line in operations]
operations = [list(map(int, nums)) for nums in operations ]

# 1
"""
Solution to Part 1
"""

def apply_operations(stacks: List[List[str]], operations: List[List[int]]):
    for operation in operations:
        count, start, end = operation

        for _ in range(count):
            to_move = stacks[start-1].pop()
            stacks[end-1].append(to_move)

stacks_copy = copy.deepcopy(stacks)
_ = apply_operations(stacks_copy, operations)
top = [stack[-1] for stack in stacks_copy]
ans = ''.join(top)

print("Part One : " + str(ans))

# 2
"""
Solution to Part 2
"""
def apply_operations_new(stacks: List[List[str]], operations: List[List[int]]):
    for operation in operations:
        count, start, end = operation

        to_move = []
        for _ in range(count):
            to_move.append(stacks[start-1].pop())

        stacks[end-1].extend(reversed(to_move))

stacks_copy = copy.deepcopy(stacks)
_ = apply_operations_new(stacks_copy, operations)
top = [stack[-1] for stack in stacks_copy]
ans = ''.join(top)

print("Part Two : " + str(ans))
