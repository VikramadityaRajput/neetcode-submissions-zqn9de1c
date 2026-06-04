class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        right = 0
        maxL = 0
        counts = {}
        while right < len(s):
            if s[right] not in counts:
                counts[s[right]] = 1
            else:
                counts[s[right]] += 1
            windowlen = right - left + 1
            if windowlen - max(counts.values()) <= k:
                maxL = max(maxL, windowlen)
                right += 1
            else:
                counts[s[left]] -= 1
                left += 1
                right += 1
        return maxL