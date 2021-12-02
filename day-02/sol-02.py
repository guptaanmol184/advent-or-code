
def get_command(line):
    splitInput = line.strip().split()
    return (splitInput[0], int(splitInput[1]))

input_commands = []
with open ('input.txt', 'r') as commandsFile:
    input_commands = [get_command(line) for line in commandsFile.readlines()]

# Part 1
horizontal_position = 0
depth = 0

for action, magnitude in input_commands:
    if action == 'forward':
        horizontal_position += magnitude
    elif action == 'up':
        depth -= magnitude
    elif action == 'down':
        depth += magnitude

print(horizontal_position * depth)

# Part 2
horizontal_position = 0
depth = 0
aim = 0

for action, magnitude in input_commands:
    if action == 'forward':
        horizontal_position += magnitude
        depth += aim * magnitude
    elif action == 'up':
        aim -= magnitude
    elif action == 'down':
        aim += magnitude

print(horizontal_position * depth)