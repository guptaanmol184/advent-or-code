
# Advent of code Year 2022 Day 02 solution
# Author = Anmol Gupta
# Date = December 2022

opponent_rpc_converter = {
    'A': 'r',
    'B': 'p',
    'C': 's'
}

my_rpc_converter = {
    'X': 'r',
    'Y': 'p',
    'Z': 's'
}

my_move_converter = {
    ('r', 'X'): 's',
    ('r', 'Y'): 'r',
    ('r', 'Z'): 'p',

    ('p', 'X'): 'r',
    ('p', 'Y'): 'p',
    ('p', 'Z'): 's',

    ('s', 'X'): 'p',
    ('s', 'Y'): 's',
    ('s', 'Z'): 'r',
}

input = list()
puzzle1 = list()
puzzle2 = list()
with open("input.txt", 'r') as input_file:
    input = input_file.readlines()
    for line in input:
        opponent, my = line.strip().split()
        puzzle1.append(
            (opponent_rpc_converter[opponent], my_rpc_converter[my]))
        opponent_rpc = opponent_rpc_converter[opponent]
        puzzle2.append((opponent_rpc,
                        my_move_converter[(opponent_rpc, my)]))

my_move_score = {
    'r': 1,
    'p': 2,
    's': 3
}
outcome_score = {
    ('r', 'r'): 3,
    ('p', 'p'): 3,
    ('s', 's'): 3,

    ('r', 's'): 0,
    ('s', 'p'): 0,
    ('p', 'r'): 0,

    ('s', 'r'): 6,
    ('p', 's'): 6,
    ('r', 'p'): 6
}


def score_round(moves):
    score = 0
    score += my_move_score[moves[1]]
    score += outcome_score[moves]
    return score


# 1
"""
Solution to Part 1
"""
ans1 = sum(map(score_round, puzzle1))
print("Part One : " + str(ans1))

# 2
"""
Solution to Part 2
"""
ans2 = sum(map(score_round, puzzle2))
print("Part Two : " + str(ans2))
