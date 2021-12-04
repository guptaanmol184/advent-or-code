class Board:
    def __init__(self, board: list[list[int]]) -> None:
        self._board = [[[num, False] for num in row] for row in board]

    def __str__(self) -> str:
        board_str = ""
        for row in self._board:
            row_str = ",".join([f"({num},{1 if filled else 0})" for num, filled in row])
            board_str = board_str + "\n" + row_str
        return board_str

    def mark_num(self, num: int) -> bool:
        for row in self._board:
            for pair in row:
                if pair[0] == num:
                    pair[1] = True

        return self._is_win()

    def _is_win(self) -> bool:

        # check row victory
        for row in self._board:
            victory = True
            for pair in row:
                if pair[1] == False:
                    victory = False
                    break

            if victory:
                return True

        # check column victory
        for column_idx in range(len(self._board[0])):
            victory = False
            for row in self._board:
                pair = row[column_idx]
                if pair[1] == False:
                    victory = False
                    break

            if victory:
                return True

        return False

    def score(self) -> int:
        sum_unmarked: int = 0
        for row in self._board:
            for pair in row:
                if pair[1] == False:
                    sum_unmarked += pair[0]

        return sum_unmarked
