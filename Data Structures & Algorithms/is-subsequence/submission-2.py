class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #reconstruction of s using chars from t
        if not s:
            return True
        word = ""
        for i in range(len(t)):
            if t[i] == s[len(word)]:
                word += t[i]
            if word == s:
                return True
        if word == s:
            return True
        return False