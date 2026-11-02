class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def dfs(o, c):
            # bc: all parenthesis are used
            if o == 0 and c == 0: 
                res.append("".join(cur))
                return
            
            # add open if we have any
            if o > 0:
                cur.append('(')
                dfs(o - 1, c) 
                cur.pop()     
            # add closed if we have them
            if c > o:
                cur.append(')')
                dfs(o, c - 1) 
                cur.pop()     
        dfs(n, n)
        return res