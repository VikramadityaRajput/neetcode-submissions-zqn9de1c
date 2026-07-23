class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            #test if we have the target
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]: # checking if the left half is sorted
                if nums[left] <= target < nums[mid]: # target present?
                    right = mid - 1
                else:
                    left = mid + 1
            else: # if not, then the right half is sorted
                if nums[mid] < target <= nums[right]: #target present?
                    left = mid + 1
                else:
                    right = mid - 1
        return -1