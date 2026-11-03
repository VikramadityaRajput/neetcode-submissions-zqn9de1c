class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word): #base case of exiting is if length is the same
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r, c) in path):
                return False #all out of bounds checks or repeated check

            path.add((r,c)) 
            res = (dfs(r+1,c,i+1) or dfs(r,c+1,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1)) #go 4 ways

            path.remove((r,c))
            return res
        
        for r in range(rows): #call it on every single point on the board
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False