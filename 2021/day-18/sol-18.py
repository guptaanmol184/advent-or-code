# Advent of code Year 2021 Day 18 solution
# Author = Anmol Gupta
# Date = December 2021

import functools
import math


def load_input_file(file_name: str):
    with open(file_name) as file:
        yield from (line.strip() for line in file)


def parse(task_input):
    for line in task_input:
        yield eval(line)


def get_elements(a, level):
    for s in a:
        if s.__class__ == list:
            yield from get_elements(s, level + 1)
        else:
            yield s, level


def to_rep(a):
    return list(get_elements(a, 0))


def explode(elements):
    for i, e in enumerate(elements):
        if e[1] == 4:
            if i > 0:
                elements[i - 1] = (elements[i - 1][0] + e[0], elements[i - 1][1])

            if i + 2 < len(elements):
                elements[i + 2] = (
                    elements[i + 2][0] + elements[i + 1][0],
                    elements[i + 2][1],
                )

            elements[i] = (0, 3)

            if i + 1 < len(elements):
                elements[i + 1] = None

            return list(filter(lambda s: s != None, elements)), True

    return elements, False


def split(elements):
    for i, e in enumerate(elements):
        if e[0] >= 10:
            return (
                elements[:i]
                + [(math.floor(e[0] / 2), e[1] + 1), (math.ceil(e[0] / 2), e[1] + 1)]
                + elements[i + 1 :],
                True,
            )

    return elements, False


def s_sum(sa, sb):
    tmp = []

    for a in sa:
        tmp.append((a[0], a[1] + 1))

    for a in sb:
        tmp.append((a[0], a[1] + 1))

    while True:
        tmp, x = explode(tmp)
        if x == True:
            continue

        tmp, y = split(tmp)
        if y == True:
            continue

        break

    return tmp


def magni_red(lit, level):
    for i, s in enumerate(lit):
        if s[1] == level:
            lit[i] = (lit[i][0] * 3 + 2 * lit[i + 1][0], lit[i][1] - 1)
            lit[i + 1] = None
            return list(filter(lambda s: s != None, lit)), True

    return lit, False


def magnitute(lit):
    c = True
    while c:
        lit, c = magni_red(lit, 3)
    c = True

    while c:
        lit, c = magni_red(lit, 2)

    c = True
    while c:
        lit, c = magni_red(lit, 1)

    assert len(lit) == 2
    return lit[0][0] * 3 + 2 * lit[1][0]


assert magnitute(list(get_elements([[1, 2], [[3, 4], 5]], 0))) == 143
assert (
    magnitute(list(get_elements([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]], 0))) == 1384
)
assert magnitute(list(get_elements([[[[1, 1], [2, 2]], [3, 3]], [4, 4]], 0))) == 445
assert magnitute(list(get_elements([[[[3, 0], [5, 3]], [4, 4]], [5, 5]], 0))) == 791
assert magnitute(list(get_elements([[[[5, 0], [7, 4]], [5, 5]], [6, 6]], 0))) == 1137
assert (
    magnitute(
        list(
            get_elements(
                [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]], 0
            )
        )
    )
    == 3488
)


def solution_for_first_part(task_input):
    result = functools.reduce(
        s_sum, map(lambda line: list(get_elements(line, 0)), parse(task_input))
    )
    return magnitute(result)


def solution_for_second_part(task_input):

    max_magnitude = 0
    nums = list(map(lambda line: list(get_elements(line, 0)), parse(task_input)))
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            x = nums[i]
            y = nums[j]

            s = s_sum(x, y)
            m = magnitute(s)
            if m > max_magnitude:
                max_magnitude = m

            s = s_sum(y, x)
            m = magnitute(s)
            if m > max_magnitude:
                max_magnitude = m

    return max_magnitude


example_input = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""".splitlines()

assert solution_for_first_part(example_input) == 4140

ans1 = solution_for_first_part(list(load_input_file("input.txt")))
ans2 = solution_for_second_part(list(load_input_file("input.txt")))

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
