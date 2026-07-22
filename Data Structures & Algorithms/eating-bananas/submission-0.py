class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        while left <= right:
            mid = (left + right) // 2 #now we test the middle point
            test = 0
            for p in piles:
                test += -(p // -mid)
            if test <= h:
                res = min(mid, res)
                right = mid - 1
            else:
                left = mid + 1
        return res
            


