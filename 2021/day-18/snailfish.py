from __future__ import annotations
import math


def parse_snailfish_num(input: str) -> list[tuple[int, int]]:
    parsed_num = []
    lvl = -1
    for ch in input:
        if ch == "[":
            lvl += 1
        elif ch == "]":
            lvl -= 1
        elif ch == ",":
            continue
        else:
            num = int(ch)
            parsed_num.append((num, lvl))

    return parsed_num


def add_snailfish_nums(
    num1: list[tuple[int, int]], num2: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    out = []
    out.extend(num1)
    out.extend(num2)
    # shift one down
    for idx, item in enumerate(out):
        updated_item = (item[0], item[1] + 1)
        out[idx] = updated_item

    # reduce num
    while True:
        is_changed = False
        for idx, num in enumerate(out):
            # explode condition
            if num[1] == 4:
                # do explode
                # pair to explode - idx, idx + 1
                left_literal = out[idx]
                right_literal = out[idx + 1]
                # assert (
                #     left_literal[1] == right_literal[1]
                # ), "Pair to explode has different levels"

                if idx - 1 != -1:
                    current = out[idx - 1]
                    out[idx - 1] = (current[0] + left_literal[0], current[1])
                if idx + 2 != len(out):
                    current = out[idx + 2]
                    out[idx + 2] = (current[0] + right_literal[0], current[1])

                # anhilate the exploded pair
                out[idx] = (0, 3)

                # remove the right literal from the pair
                del out[idx + 1]

                is_changed = True
                break
            # split condition
            if num[0] >= 10:
                n = num[0]
                lvl = num[1]
                out[idx] = (math.floor(n / 2), lvl + 1)
                out.insert(idx + 1, (math.ceil(n / 2), lvl + 1))
                is_changed = True
                break
        if is_changed == False:
            break

    return out
