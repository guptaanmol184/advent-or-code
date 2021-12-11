# Advent of code Year 2021 Day XX solution
# Author = Anmol Gupta
# Date = December 2021

input = list()
with open("input.txt", "r") as input_file:
    input = input_file.readlines()


def print_octopus_state(octopus_state):
    print("{")
    for i in range(10):
        print("[", end="")
        for j in range(10):
            if j != 9:
                print("{:3d}".format(octopus_state[i][j]), end=",")
            else:
                print("{:3d}".format(octopus_state[i][j]), end="")
        print("]")
    print("}")


octopus_state = [list(map(int, list(line.strip()))) for line in input]
flash_count = 0
step = 0
step_200_flash_count = 0
synchronised_flash_step = 0

while True:
    # Increment step
    step += 1

    # No flashes initially
    flashed = [[False for _ in range(10)] for _ in range(10)]

    # Increment energy
    for i in range(10):
        for j in range(10):
            octopus_state[i][j] += 1

    # Exhaust flashes
    while True:
        prev_flash_count = flash_count
        for i in range(10):
            for j in range(10):
                if octopus_state[i][j] > 9 and flashed[i][j] == False:
                    # flash
                    flashed[i][j] = True
                    flash_count += 1

                    # increment neighbour energy
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            x = i + di
                            y = j + dj
                            if x != -1 and x != 10 and y != -1 and y != 10:
                                octopus_state[x][y] += 1
                                # print(
                                #    f"flash from {i} {j} successfully changed {x} {y}"
                                # )
                                # print_octopus_state(octopus_state)

        # break if no new flashes
        if prev_flash_count == flash_count:
            break

    # Reset energies, and check if it were a synchronised flash
    did_all_flash = True
    for i in range(10):
        for j in range(10):
            if flashed[i][j] == True:
                octopus_state[i][j] = 0
            else:
                did_all_flash = False

    if step == 100:
        step_200_flash_count = flash_count

    if did_all_flash:
        synchronised_flash_step = step
        break


# 1
"""
Solution to Part 1
"""
print("Part One : " + str(step_200_flash_count))

# 2
"""
Solution to Part 2
"""
print("Part Two : " + str(synchronised_flash_step))
