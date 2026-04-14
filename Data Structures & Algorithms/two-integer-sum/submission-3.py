class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newmap = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in newmap:
                return [newmap[difference], i]
            newmap[n] = i
        