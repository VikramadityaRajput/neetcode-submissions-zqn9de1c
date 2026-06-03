class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        check = sorted(s1)
        k1 = len(s2) - k
        ptr = 0
        while ptr <= k1:
            if sorted(s2[ptr:ptr + k]) == check:
                return True
            ptr += 1
        return False