class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        tbl = {}
        for y in range(len(board)):
            column = y
            for x in range(len(board[y])):
                row = x
                if board[y][x] == ".": continue
                if board[y][x] in tbl.values():
                    filtered = {k: v for k, v in tbl.items() if v == board[y][x]}
                    for (old_row, old_col), value in filtered.items():
                        if column == old_col: return False
                        if row == old_row: return False
                        if (row // 3) == (old_row // 3) and (column // 3) == (old_col // 3):
                            return False

                tbl[tuple([row, column])] = board[y][x]\

        return True

                
