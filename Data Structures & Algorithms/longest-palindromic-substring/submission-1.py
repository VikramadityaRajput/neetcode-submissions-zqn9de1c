class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        reslen = 0
        
        for i in range(n):
            # odd lengths
            j = 0 
            while i - j >= 0 and i + j < n and s[i - j] == s[i + j]:
                current_len = (i + j) - (i - j) + 1
                if current_len > reslen:
                    reslen = current_len
                    res = s[i - j : i + j + 1]
                j += 1 
            j = 0 
            #even lengths
            while i - j >= 0 and i + 1 + j < n and s[i - j] == s[i + 1 + j]:
                current_len = (i + 1 + j) - (i - j) + 1
                if current_len > reslen:
                    reslen = current_len
                    res = s[i - j : i + 1 + j + 1]
                j += 1

        return res