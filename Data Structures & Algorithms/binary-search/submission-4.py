class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursive_search(left: int, right: int) -> int:
            if left > right: #if it doesnt exist
                return -1
            mid = (left + right) // 2 #track the index
            
            if nums[mid] == target: #initial check
                return mid
            elif target > nums[mid]: #traverse left or right
                return recursive_search(mid + 1, right)
            else:
                return recursive_search(left, mid - 1)
        return recursive_search(0, len(nums) - 1)