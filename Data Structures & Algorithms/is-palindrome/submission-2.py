class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_without_alnum = ""
        for i in range(len(s)):
            if s[i].isalnum():
                s_without_alnum += s[i].lower()
        return s_without_alnum == s_without_alnum[::-1]
