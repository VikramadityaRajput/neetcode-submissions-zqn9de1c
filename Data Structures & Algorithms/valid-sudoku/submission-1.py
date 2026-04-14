class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check by each row easiest
        for i in range(9):
            row_vals = [val for val in board[i] if val != "."]
            if len(row_vals) != len(set(row_vals)):
                return False
        #check by each column next easy
        for i in range(9):
            col_vals = []
            for r in range(9):
                cell_value = board[r][i]
                if cell_value != ".":
                    col_vals.append(cell_value)
            if len(col_vals) != len(set(col_vals)):
                return False
        for box_row in range(3):
            for box_col in range(3):
                box_vals = []

                for r in range(3):
                    for c in range(3):
                        cell_value = board[box_row*3 + r][box_col*3 + c]
                        if cell_value != ".":
                            box_vals.append(cell_value)
                if len(box_vals) != len(set(box_vals)):
                    return False
        return True