class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #just iterate through and track the currnet min and max product
        #if you encounter a 0 save your progress
        #maybe i store a negative dp so that if theres a negative it can get negated
        if not nums:
            return 0
        n = len(nums)
        res = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

    
        for i in range(1, n): #kadane's algorithm
            temp_max = max(nums[i], cur_max * nums[i], cur_min * nums[i]) #if a negative got scaled up or a positive got scaled down or if either one go to 0 itll make the proper update
            cur_min = min(nums[i], cur_max * nums[i], cur_min * nums[i]) #same thing here but itll pick the most negative value 
            cur_max = temp_max #update the max
            res = max(res, cur_max) 
        return res

