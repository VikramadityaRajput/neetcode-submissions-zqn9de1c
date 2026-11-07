class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * 101 #cost of making it past the second step is the cheapest previous2
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i-1], cost[i - 2] + dp[i - 2]) 
        return dp[n]