class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # think about it in terms of decision trees
        # you either do something or you don't
        res = []
        combo = []
        def dfs(i, combo, total):
            if total == target:
                res.append(combo.copy()) #copy because reference is modified
                return
            if i >= len(nums) or total > target:
                return 
            # you either add what ur looking at or add nothing and increment i
            combo.append(nums[i]) #go down the tree and add what ur looking at
            dfs(i, combo, total + nums[i])

            combo.pop() # undo that change
            dfs(i + 1, combo, total) #go down the tree with the next element
        dfs(0, [], 0)
        return res
