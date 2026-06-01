class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nn = sorted(nums) # have to handle duplicates can either set or handle it in runs
        runs = []
        run = 1
        for i in range(len(nums) - 1):
            if nn[i+1] == nn[i] + 1:
                run += 1
            elif nn[i+1] == nn[i]:
                continue
            else:
                runs.append(run)
                run = 1
        runs.append(run)
        return max(runs)