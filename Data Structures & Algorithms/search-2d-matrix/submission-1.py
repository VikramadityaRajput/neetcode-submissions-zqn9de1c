class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search on if the elemtn is between the elemtb of the given row
        rows, cols = len(matrix), len(matrix[0])
        up, down = 0, rows - 1
        while up <= down:
            mid = (up + down) // 2
            if target < matrix[mid][0]: #binary search on the rows
                down = mid - 1 
            elif target > matrix[mid][-1]:
                up = mid + 1
            else:
                break
        if not (up <= down):
            return False
        #now we know we're in the right row
        left, right = 0, cols - 1
        while left <= right:
            m = (left + right) // 2
            if target < matrix[mid][m]:
                right = m - 1
            elif target > matrix[mid][m]:
                left = m + 1 
            else:
                return True
        return False
    

