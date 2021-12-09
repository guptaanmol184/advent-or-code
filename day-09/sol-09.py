# Advent of code Year 2021 Day XX solution
# Author = Anmol Gupta
# Date = December 2021

input = list()
with open("input.txt", "r") as input_file:
    input = input_file.readlines()

heightmap = [list(map(int, list(line.strip()))) for line in input]

x_size = len(heightmap)
y_size = len(heightmap[0])
lowest_points = []

# 1
for i in range(0, x_size):
    for j in range(0, y_size):
        top = heightmap[i - 1][j] if i - 1 != -1 else 10
        bottom = heightmap[i + 1][j] if (i + 1) != x_size else 10
        left = heightmap[i][j - 1] if j - 1 != -1 else 10
        right = heightmap[i][j + 1] if (j + 1) != y_size else 10

        min_adjacents = min(top, bottom, left, right)
        curr = heightmap[i][j]
        if curr < min_adjacents:
            lowest_points.append((i, j))

risk_level_sum = 0
for i, j in lowest_points:
    risk_level_sum += heightmap[i][j] + 1

print("Part One : " + str(risk_level_sum))

# 2
# Multiply sizes of 3 largest basins

print("Part Two : " + str(None))
