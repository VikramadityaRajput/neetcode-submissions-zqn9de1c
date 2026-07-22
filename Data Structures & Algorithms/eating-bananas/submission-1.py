class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        while left <= right:
            mid = (left + right) // 2 #now we test the middle point
            test = 0
            for p in piles:
                test += -(p // -mid) 
            if test <= h: #check how many hours it takes and if condition is satisfied
                res = min(mid, res) #if the condition is met check and adjust
                right = mid - 1
            else:
                left = mid + 1
        return res #once you've exited the loop you can return
            


