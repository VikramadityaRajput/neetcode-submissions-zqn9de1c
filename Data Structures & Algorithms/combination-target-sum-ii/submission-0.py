class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        candidates.sort() #sorted order so that we can just skip over repeats

        def dfs(i, combo, total):
            if (total == target): #base case 1
                res.append(combo.copy())
                return
            if (i >= len(candidates) or total > target): #base case 2
                return 
            combo.append(candidates[i]) # you either take the next number or possibly take the duplicate
            dfs(i + 1, combo, total + candidates[i])
            combo.pop() #choose instead to skip to the next number
            while (i < len(candidates) - 1 and candidates[i] == candidates[i + 1] ):
                i += 1
            dfs(i + 1, combo, total)
        dfs(0, [], 0)
        return res