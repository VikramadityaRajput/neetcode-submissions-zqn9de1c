class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * 46
        dp[1], dp[2], dp[3] = 1,2,3
        for i in range(4,n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
