class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {")" : "(", "}" : "{", "]" : "["}
        for i in range(len(s)):
            if s[i] not in dictionary:
                stack.append(s[i])
            elif s[i] in dictionary:
                if len(stack) == 0:
                    return False
                if stack[-1] != dictionary[s[i]]:
                    return False
                stack.pop(-1)
        return not stack
