class Solution:
    def trap(self, height: List[int]) -> int:
         #find the highest wall at every position
         #solve this using two pointer u start at adjacent, work down one at a time and save the max
        total = 0
        for i in range(1, len(height) - 1, 1):
            left = i - 1 
            right = i + 1
            mxl = []
            mxr = []
            while left >= 0:
                mxl.append(height[left])
                left -= 1
            while right < len(height):
                mxr.append(height[right])
                right += 1      
            lowest = min(max(mxr), max(mxl))
            total += max(lowest - height[i], 0)
        return total

