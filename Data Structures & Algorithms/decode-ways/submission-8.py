class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = [0] * (n + 1) #track the previous ways dp[i] is the ways to decode a string of i length 
        if s[0] == '0': #invalid
            return 0
        dp[0] = 1 #1 way to decode an empty string
        dp[1] = 1 #1 way to decode a string of length 1
        for i in range(2, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i-1]
            
            two_d = int(s[i - 2 : i])
            if 10 <= two_d <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

