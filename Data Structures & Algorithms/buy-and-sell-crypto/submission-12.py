class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0  
        B = 0
        S = 1
        mp = 0
        while S < len(prices):
            profit = prices[S] - prices[B]
            if prices[S] > prices[B]:
                mp = max(mp, profit)
            else:
                B = S
            S += 1
        return mp