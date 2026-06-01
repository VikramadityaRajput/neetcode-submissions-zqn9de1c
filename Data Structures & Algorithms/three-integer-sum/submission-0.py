class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #it seems like were just doing 2sum n times since index doesnt matter we can sort
        res = []
        valid = set()
        newnum = sorted(nums) #target = 0
        for i in range(len(nums)):
            target = -1 * newnum[i]
            l = i + 1
            r = len(newnum) - 1
            while l < r:
                total = newnum[l] + newnum[r]
                if total == target:
                    solution = [newnum[i], newnum[l], newnum[r]]
                    sol = "".join(str(solution))
                    if sol not in valid:
                        valid.add(sol)
                        res.append(solution)
                    l += 1
                    r -= 1
                elif total > target:
                    r -= 1
                else:
                    l += 1
        return res