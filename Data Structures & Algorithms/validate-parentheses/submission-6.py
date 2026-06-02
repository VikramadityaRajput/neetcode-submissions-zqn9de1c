class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pars = {'{' : '}', '[' : ']', '(' : ')'}
        for i in range(len(s)):
            if s[i] in pars:
                stack.append(s[i])
            if s[i] in pars.values() and (len(stack) == 0 or s[i] != pars[stack[-1]]):
                return False
            if s[i] == pars[stack[-1]]:
                stack.pop()
            
        if len(stack) == 0:
            return True
        else:
            return False