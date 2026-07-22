class Solution:
    def findMin(self, nums: List[int]) -> int:
        #break it in half
        #if the start of left is less than the start of right, then left is sorted. right contains the restart
        res = nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[left] <= nums[mid]: #right one isnt sorted
                left = mid + 1
            else:
                right = mid - 1 #adjust the pointers 
        return res
