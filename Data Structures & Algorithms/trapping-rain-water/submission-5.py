class Solution:
    def trap(self, height: List[int]) -> int:
         #find the highest wall at every position
         #solve this using two pointer u start at adjacent, work down one at a time and save the max
        total = 0
        for i in range(1, len(height) - 1, 1):
            left = max(height[:i])
            right = max(height[i:])
            lowest = min(left, right)
            total += max(lowest - height[i], 0)
        return total

