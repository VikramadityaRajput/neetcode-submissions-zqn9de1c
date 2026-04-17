class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        newmap = {}
        for i, n in enumerate(numbers):
            difference = target - n
            if difference in newmap:
                return [newmap[difference] + 1, i + 1]
            newmap[n] = i