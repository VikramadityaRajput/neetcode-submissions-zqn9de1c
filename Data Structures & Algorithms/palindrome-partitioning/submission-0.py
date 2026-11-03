class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []
        #at each possible index i either partition or i dont partition. 
        # i then do that for every index so i have every possible partition.
        #the base case where i exit is when i >= s
        def dfs(i):
            if i >= len(s): #base case to exit
                res.append(cur.copy())
                return
            for j in range(i, len(s), 1):
                temp = s[i:j+1] #checking if the partition is a palindrome
                if temp == temp[::-1]:
                    cur.append(temp) #append if it is
                    dfs(j + 1) 
                    cur.pop()
        dfs(0)
        return res

    