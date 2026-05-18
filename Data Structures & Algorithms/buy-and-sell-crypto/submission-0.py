class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small = 100
        large = 0
        for price in prices:
            if price < small:
                small = price
            elif price - small > large:
                large = price - small
        return large
            