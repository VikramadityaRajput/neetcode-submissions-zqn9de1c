class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#maybe we can call word break recursively on smaller and smaller portions of the word
        dp = {}

        def check(curr):
            if curr in dp: #if your string is already in the save then no need to check
                return dp[curr]
            n = len(s)
            if curr in wordDict: #original logic just nested
                return True
            for i in range(n): #original recursive logic to check smaller and smaller portions of the word
                if curr[:i + 1] in wordDict:
                    if check(curr[i + 1:]):
                        dp[curr] = True
                        return True
            dp[curr] = False #if it didnt get caught by any of the words its false
            return False
        return check(s)
            