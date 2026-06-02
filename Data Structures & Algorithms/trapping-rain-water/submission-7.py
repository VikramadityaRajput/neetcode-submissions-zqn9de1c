class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: #
            return 0
        #Two Pointers starting at the far left and right edges
        l, r = 0, len(height) - 1     
        left_max, right_max = height[l], height[r]
        total = 0
        while l < r:
            if left_max < right_max:
                l += 1
                # Update the highest wall seen on the left
                left_max = max(left_max, height[l])
                # Add trapped water (if height[l] is the new max, this just adds 0)
                total += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                total += right_max - height[r]
                
        return total