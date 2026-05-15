class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            d[n] = i
        for i, n in enumerate(nums):
            t = target - n
            if (t in d and d[t] != i):
                return [i, d[t]]