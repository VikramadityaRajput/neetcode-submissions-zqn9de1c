class Solution:
    def rob(self, nums: List[int]) -> int:
        #maybe saved the best dp where they rob first and dont rob first house?
        ndp = [0] * 101
        dp = [0] * 101
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        if n == 3:
            return max(nums[0], nums[1], nums[2])
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = dp[0] + nums[2]
        for i in range(3, n-1):
            dp[i] = max(dp[i - 2], dp[i-3]) + nums[i]
        m1 = max(dp[n-2], dp[n-3])

        ndp[1] = nums[1]
        ndp[2] = nums[2]
        for i in range(3, n):
            ndp[i] = max(ndp[i-2], ndp[i-3]) + nums[i]
        m2 = max(ndp[n-1], ndp[n-2])
        return max(m1, m2)