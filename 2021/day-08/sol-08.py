# Advent of code Year 2021 Day XX solution
# Author = Anmol Gupta
# Date = December 2021


input = list()
with open("input.txt", "r") as input_file:
    input = input_file.readlines()

# 1 Let us try some map-reduce action
import functools

ans1 = sum(
    map(
        lambda x: functools.reduce(
            lambda a, b: a + 1 if b in [2, 3, 4, 7] else a,
            list(map(len, x.strip().split("|")[1].strip().split(" "))),
            0,
        ),
        input,
    )
)

## pip install pyfunctional
# from functional import seq
#
# a = (
#     seq(input)
#     .map(lambda x: x.split("|"))
#     .map(lambda x: x[1].strip())
#     .map(lambda x: x.split(" "))
#     .map(lambda x: len(x))
#     .flatten()
#     .filter(lambda x: x in [2, 3, 4, 7])
#     .sum()
# )
# print(a)


# print("Part One : " + str(ans1))

# 2
def identify_1_4_7_8(all_numbers: list[set[str]], identified: dict[int, set[str]]):
    for num in all_numbers:
        if len(num) == 2:
            identified[1] = num
        elif len(num) == 3:
            identified[7] = num
        elif len(num) == 4:
            identified[4] = num
        elif len(num) == 7:
            identified[8] = num


def identify_3(all_numbers: list[set[str]], identified: dict[int, set[str]]):
    for num in all_numbers:
        if len(num) == 5 and identified[1] < num:
            identified[3] = num
            return


def identify_2_5(all_numbers: list[set[str]], identified: dict[int, set[str]]):
    four_but_not_one_segments = identified[4] - identified[1]
    for num in all_numbers:
        if len(num) == 5 and num != identified[3]:
            if num > four_but_not_one_segments != 0:
                identified[5] = num
            else:
                identified[2] = num


def identify_9(all_numbers: list[set[str]], identified: dict[int, set[str]]):
    for num in all_numbers:
        if len(num) == 6 and num > identified[3] and num > identified[5]:
            identified[9] = num
            return


def identify_0_6(all_numbers: list[set[str]], identified: dict[int, set[str]]):
    for num in all_numbers:
        if len(num) == 6 and num != identified[9]:
            if num > identified[1]:
                identified[0] = num
            else:
                identified[6] = num


def get_display_num(display, identified):
    display_num = 0
    for digit_segments in display:
        for num, segments in identified.items():
            if segments == digit_segments:
                display_num = display_num * 10 + num
    return display_num


ans2 = 0

for idx, line in enumerate(input):
    identified = {}
    all_numbers, display = line.strip().split(" | ")

    all_numbers = [set(digit) for digit in all_numbers.strip().split(" ")]

    # identify the digits
    identify_1_4_7_8(all_numbers, identified)
    identify_3(all_numbers, identified)
    identify_2_5(all_numbers, identified)
    identify_9(all_numbers, identified)
    identify_0_6(all_numbers, identified)

    # read the display
    display = [set(digit) for digit in display.strip().split(" ")]
    display_num = get_display_num(display, identified)

    ans2 += display_num


print("Part Two : " + str(ans2))
