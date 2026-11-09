class Solution:
    def countSubstrings(self, s: str) -> int:
        #basically the same as longest palidromic substring but u dont need to track the longest
        n = len(s)
        res = 0
        for i in range(n):
            j = 0
            while i - j >= 0 and i + j < n and s[i - j] == s[i + j]: # for the odd case
                j += 1 #just keep expanding ur palindrome while u can
                res += 1
            j = 0
            while i - j >= 0 and i + j + 1 < n and s[i-j] == s[i + j +1]: # for the even case
                j += 1 #just keep pushing ur palindrome while u can
                res += 1
        return res