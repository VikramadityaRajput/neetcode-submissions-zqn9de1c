class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1: #base case if only 1 number left
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0) #remove the first number and recurse
            perms = self.permute(nums) 
            
            for perm in perms: #add the number we removed to the end
                perm.append(n)

            res.extend(perms)
            nums.append(n)

        return res