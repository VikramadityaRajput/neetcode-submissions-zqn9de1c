class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows, check columns, and then check 3x3s
        for i in range(9):
            nums = []
            for j in range(9):
                if board[i][j] != '.':
                    nums.append(board[i][j])
            if len(set(nums)) != len(nums):
                return False
        for i in range(9):
            nums = []
            for j in range(9):
                if board[j][i] != '.':
                    nums.append(board[j][i])
            if len(set(nums)) != len(nums):
                return False
        for k in range(3):
            for l in range(3):
                nums = []
                for i in range(3): 
                    for j in range(3):
                        if board[i + 3 * k][j + 3 * l] != '.':
                            nums.append(board[i + 3 * k][j + 3 * l])
                if len(set(nums)) != len(nums):
                    return False
        return True