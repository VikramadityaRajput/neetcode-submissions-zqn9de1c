class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []

        def dfs(i):
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            dfs(i + 1)

            cur.pop() #take the other route and not include that number
            while (i < len(nums) - 1 and nums[i] == nums[i+1]):
                i += 1 # now were at the next number
            dfs(i + 1)
        dfs(0)
        return res
            
