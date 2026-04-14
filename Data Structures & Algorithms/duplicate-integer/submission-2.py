class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copy = []
        for num in nums:
            if num in copy:
                return True
            copy.append(num)
        return False
        