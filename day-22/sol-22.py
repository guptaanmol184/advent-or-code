# Advent of code Year 2021 Day XX solution
# Author = Anmol Gupta
# Date = December 2021

input = list()
with open("input.txt", "r") as input_file:
    input = input_file.readlines()

# parse instructions from input
def parse_input(input):
    for line in input:
        on_off, cuboid_defination = line.strip().split(" ")
        on_off_inst = on_off == "on"

        range_insts = []
        for range in cuboid_defination.split(","):
            range_insts.extend(list(map(int, range.split("=")[1].split(".."))))

        yield (on_off_inst, *range_insts)


import itertools


def first_solution(instructions):
    """
    input: instructions for rebooting the cube
    output: number of cubes that are on
    """
    on_cubes = set()
    for inst in instructions:
        on_off, xlow, xhigh, ylow, yhigh, zlow, zhigh = inst
        # thresholding in valid range
        xlow = max(-50, xlow)
        xhigh = min(50, xhigh)
        ylow = max(-50, ylow)
        yhigh = min(50, yhigh)
        zlow = max(-50, zlow)
        zhigh = min(50, zhigh)
        for item in itertools.product(
            range(xlow, xhigh + 1), range(ylow, yhigh + 1), range(zlow, zhigh + 1)
        ):
            if on_off:
                on_cubes.add(item)
            else:
                if item in on_cubes:
                    on_cubes.remove(item)

    return len(on_cubes)


def second_solution(instructions):
    """
    input: instructions for rebooting the cube
    output: number of cubes that are on
    """
    cubes = []

    for inst in instructions:
        [op, ux, vx, uy, vy, uz, vz] = inst
        for cubes_i in range(len(cubes)):
            [ux2, vx2, uy2, vy2, uz2, vz2] = cubes[cubes_i]
            if (
                ux > vx2 or vx < ux2 or uy > vy2 or vy < uy2 or uz > vz2 or vz < uz2
            ):  # new on zone not overlapping existing on zone
                continue
            cubes[cubes_i] = None
            if ux > ux2:
                cubes.append((ux2, ux - 1, uy2, vy2, uz2, vz2))
            if vx < vx2:
                cubes.append((vx + 1, vx2, uy2, vy2, uz2, vz2))
            if uy > uy2:
                cubes.append((max(ux2, ux), min(vx2, vx), uy2, uy - 1, uz2, vz2))
            if vy < vy2:
                cubes.append((max(ux2, ux), min(vx2, vx), vy + 1, vy2, uz2, vz2))
            if uz > uz2:
                cubes.append(
                    (
                        max(ux2, ux),
                        min(vx2, vx),
                        max(uy2, uy),
                        min(vy2, vy),
                        uz2,
                        uz - 1,
                    )
                )
            if vz < vz2:
                cubes.append(
                    (
                        max(ux2, ux),
                        min(vx2, vx),
                        max(uy2, uy),
                        min(vy2, vy),
                        vz + 1,
                        vz2,
                    )
                )
        if op == True:
            cubes.append(
                (
                    min(ux, vx),
                    max(ux, vx),
                    min(uy, vy),
                    max(uy, vy),
                    min(uz, vz),
                    max(uz, vz),
                )
            )
        cubes = [cube for cube in cubes if cube is not None]

    on_count = 0
    for cube in cubes:
        [ux, vx, uy, vy, uz, vz] = cube
        on_count += (vx - ux + 1) * (vy - uy + 1) * (vz - uz + 1)
    return on_count


"""
Solution to Part 1
"""
print("Part One : " + str(first_solution(parse_input(input))))

# 2
"""
Solution to Part 2
"""
print("Part Two : " + str(second_solution(parse_input(input))))
