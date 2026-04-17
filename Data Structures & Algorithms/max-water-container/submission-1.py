class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #product is difference in index * min of the 2 numbers
        p = 0
        #two pointers will move towards each other
        l = len(heights) - 1
        r = 0
        while l != r:
            w = abs(r - l)
            h = min(heights[r], heights[l])
            product = w * h
            if product > p:
                p = product
            if heights[r] > heights[l]:
                l -= 1
            else:
                r += 1
        return p



