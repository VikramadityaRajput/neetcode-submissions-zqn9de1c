class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) #store a default value thats higher than the possible limit
        dp[0] = 0 
        for i in range(1, amount + 1): #enter a value for each amount up until amount
            for c in coins: #compare each coin summed with the dp of amount - coin
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]