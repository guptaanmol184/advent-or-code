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


def basin_fill(x, y, heightmap, visited):

    # if value x, y not inside
    # The basin is invalid
    if x < 0 or x >= x_size:
        return 0
    if y < 0 or y >= y_size:
        return 0

    # if visited x, y return
    # The point is already visited
    if visited[x][y] == True:
        return 0

    # Mark the point for basin caculation as visited
    visited[x][y] = True

    # if value x, y is 9
    # 9 cannot be counted as a part of the basin
    if heightmap[x][y] == 9:
        return 0

    return (
        1  # current point
        + basin_fill(x + 1, y, heightmap, visited)
        + basin_fill(x - 1, y, heightmap, visited)
        + basin_fill(x, y - 1, heightmap, visited)
        + basin_fill(x, y + 1, heightmap, visited)
    )


basin_sizes = []


# Multiply sizes of 3 largest basins
for x, y in lowest_points:
    # use flood fill to identify the basins
    # mark x, y visited
    visited = [[False for _ in range(y_size)] for _ in range(x_size)]
    basin_size = basin_fill(x, y, heightmap, visited)
    basin_sizes.append(basin_size)


basin_sizes.sort(reverse=True)
ans2 = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

print("Part Two : " + str(ans2))
