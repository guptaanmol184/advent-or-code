# Advent of code Year 2021 Day XX solution
# Author = Anmol Gupta
# Date = December 2021

import functools


input = list()
with open("input.txt", "r") as input_file:
    input = input_file.readlines()

CHUNK_OPEN_CHARACTER = ["(", "[", "{", "<"]
CHUNK_CLOSE_CHARACTER = [")", "]", "}", ">"]
CHUNK_VALID_CHARACTER_PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}
CORRUPT_CHARACTER_POINTS_TABLE = {")": 3, "]": 57, "}": 1197, ">": 25137}
AUTOCOMPLETE_CHARACTER_POINTS_TABLE = {")": 1, "]": 2, "}": 3, ">": 4}

lines = [line.strip() for line in input]


def validate_line(line):
    character_stack = []
    for c in line:
        if c in CHUNK_OPEN_CHARACTER:
            character_stack.append(c)
        elif c in CHUNK_CLOSE_CHARACTER:
            a = character_stack.pop()
            if c == CHUNK_VALID_CHARACTER_PAIRS[a]:
                continue
            else:
                return ("corrupt", c)
    return (
        "incomplete",
        "".join([CHUNK_VALID_CHARACTER_PAIRS[c] for c in character_stack])[::-1],
    )


def autocomplete_score_reducer(score, c):
    score = score * 5
    score += AUTOCOMPLETE_CHARACTER_POINTS_TABLE[c]
    return score


syntax_error_score = 0
autocomplete_scores = []

# scoring
for line in lines:
    output = validate_line(line)
    if output[0] == "corrupt":
        syntax_error_score += CORRUPT_CHARACTER_POINTS_TABLE[output[1]]
    elif output[0] == "incomplete":
        autocomplete_scores.append(
            functools.reduce(autocomplete_score_reducer, output[1], 0)
        )

autocomplete_scores.sort()
middle_autocomplete_score = autocomplete_scores[len(autocomplete_scores) // 2]

# 1
print("Part One : " + str(syntax_error_score))

# 2
print("Part Two : " + str(middle_autocomplete_score))
