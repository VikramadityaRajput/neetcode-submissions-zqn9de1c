class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""

        checker = {}
        for char in t:
            checker[char] = checker.get(char, 0) + 1

        window = {}
        left = 0
        contains = 0
        req = len(checker) # Number of UNIQUE characters required
        
        # Track the [left, right] bounds of the minimum window and its length
        res_bounds = [-1, -1]
        min_len = float("infinity")
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
        
            if char in checker and window[char] == checker[char]:
                contains += 1
            while contains == req:
                current_window_len = right - left + 1
                if current_window_len < min_len:
                    res_bounds = [left, right]
                    min_len = current_window_len
                left_char = s[left]
                window[left_char] -= 1
                if left_char in checker and window[left_char] < checker[left_char]:
                    contains -= 1
                left += 1
                
        left_bound, right_bound = res_bounds
        return s[left_bound : right_bound + 1] if min_len != float("infinity") else ""