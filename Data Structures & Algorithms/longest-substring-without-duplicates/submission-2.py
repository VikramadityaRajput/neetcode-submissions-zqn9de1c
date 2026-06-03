class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #checking duplicates two pointer. once the duplicate appears you reset the pointer and advance
        left = 0 #dont forget python is end exclusive
        right = 0
        maxL = 0
        while right < len(s):
            test = s[left:right+1]
            if len(test) == len(set(test)):
                right += 1
                maxL = max(maxL, len(set(test)))
            else:
                maxL = max(maxL, len(set(test)))
                left+=1
        return maxL