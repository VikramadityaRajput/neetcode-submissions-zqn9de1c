class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp = [0] * 101
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = dp[0] + nums[2]
        for i in range(3, n):
            dp[i] = max(dp[i - 2], dp[i-3]) + nums[i]
        return max(dp[n-1], dp[n-2])
        
