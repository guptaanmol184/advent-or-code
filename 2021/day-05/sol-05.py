# Advent of code Year 2021 Day 05 solution
# Author = Anmol Gupta
# Date = December 2021

input: list = list()
with open("input.txt", "r") as input_file:
    input = input_file.readlines()


def make_point(point_str: str) -> tuple[int, int]:
    """
    Parse a point from it's string repr to tuple
    """
    return tuple(map(int, point_str.split(",")))


input = [line.strip().split(" -> ") for line in input]
lines: list[tuple[int, int]] = [
    [make_point(point) for point in point_list] for point_list in input
]
print(lines[0])

points_ctr: dict[tuple[int, int], int] = dict()

for (x1, y1), (x2, y2) in lines:
    if x1 == x2 and y1 != y2:
        x = x1
        # iterate over y
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            points_ctr[(x, y)] = points_ctr.get((x, y), 0) + 1
    elif y1 == y2 and x1 != x2:
        y = y1
        # iterate over x
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            points_ctr[(x, y)] = points_ctr.get((x, y), 0) + 1
    else:
        # Comment this else case for solution of part 1
        x_inc = 1 if x2 > x1 else -1
        y_inc = 1 if y2 > y1 else -1

        x, y = x1, y1

        if x1 > x2:
            x1, x2 = x2, x1
        for i in range(x1, x2 + 1):
            points_ctr[(x, y)] = points_ctr.get((x, y), 0) + 1
            x += x_inc
            y += y_inc

total = 0
for value in points_ctr.values():
    if value >= 2:
        total += 1

print(total)
