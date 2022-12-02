# Advent of code Year 2021 Day 04 solution
# Author = Anmol Gupta
# Date = December 2021

from bing_board import Board

input: list[str] = list()
with open("input.txt", "r") as input_file:
    input = input_file.readlines()

# Get all the numbers from the first line, split and store as int's in array bingo_num_list
bingo_num_list: list[int] = [int(num) for num in input[0].strip().split(",")]

board_list: list[Board] = []
for i in range(1, len(input), 6):
    start_index = i + 1
    board_str = input[start_index : start_index + 5]
    board_int = [[int(num) for num in row.strip().split()] for row in board_str]
    board_list.append(Board(board_int))

first_win_score: int = 0
found_first_win_final_score: bool = False
last_win_score: int = 0

for num in bingo_num_list:
    win_boards = []
    last_win_score_list = []
    for board in board_list:
        if board.mark_num(num):
            win_boards.append(board)

            if not found_first_win_final_score:
                first_win_score = board.score() * num
                found_first_win_final_score = True

            last_win_score = board.score() * num
            last_win_score_list.append(last_win_score)

    # update the board_list with non winning boards:
    board_list = [board for board in board_list if board not in win_boards]

    if not board_list:
        break

print(first_win_score)
print(last_win_score_list)
