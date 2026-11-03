class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #ig we map each number to an array of what its number could be
        phone_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv","9": "wxyz"}
        res = []
        cur = [] # we will do "".join(cur) to make it a string and then append
        if not digits: return cur
        def dfs(i): # i wil be the current number of digits were looking at
            if len(cur) == len(digits): # base case is if the length is equal
                res.append("".join(cur))
                return
            for c in phone_map[digits[i]]: #iterate over each character
                cur.append(c) #append the ith possible character
                dfs(i + 1) #recursively cal on the next character
                cur.pop() #backtrack so we can do it again
        dfs(0)
        return res
