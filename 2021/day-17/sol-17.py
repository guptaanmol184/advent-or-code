# Advent of code Year 2021 Day 17 solution
# Author = Anmol Gupta
# Date = December 2021

input = list()
with open("input.txt", "r") as input_file:
    input = input_file.readlines()

target_area = input[0].strip().split(": ")[1]
x_bounds, y_bounds = target_area.split(", ")


def get_bounds(bounds_str):
    low, high = bounds_str.split("..")
    low = low.split("=")[1]
    return (int(low), int(high))


x_low, x_high = get_bounds(x_bounds)
y_low, y_high = get_bounds(y_bounds)


def fire_probe(initial_vel_x, intial_vel_y):

    x_vel = initial_vel_x
    y_vel = intial_vel_y

    probe_position_x = 0
    probe_position_y = 0

    y_max = -10000
    hit_target = False

    while True:
        probe_position_x += x_vel
        probe_position_y += y_vel

        if probe_position_y > y_max:
            y_max = probe_position_y

        if x_vel > 0:
            x_vel -= 1
        y_vel -= 1

        if (
            probe_position_x >= x_low
            and probe_position_x <= x_high
            and probe_position_y >= y_low
            and probe_position_y <= y_high
        ):
            # success
            hit_target = True
            break

        if probe_position_x > x_high or probe_position_y < y_low:
            # stop iterating, since out of bounds
            break

    return (hit_target, y_max)


total_max_y = 0
total_nice_velocities = 0
for x in range(1000):
    for y in range(-1000, 1000):
        hit_target, y_max = fire_probe(x, y)
        if hit_target:
            total_nice_velocities += 1
        if hit_target and y_max > total_max_y:
            total_max_y = y_max

ans1 = total_max_y
ans2 = total_nice_velocities

# 1
"""
Solution to Part 1
"""
print("Part One : " + str(ans1))

# 2
"""
Solution to Part 2
"""
print("Part Two : " + str(ans2))
