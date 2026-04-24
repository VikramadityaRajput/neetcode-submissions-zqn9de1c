class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #intiailize the stack
        dictionary = {")" : "(", "}" : "{", "]" : "["} #map brackets to each other when checking 'equality'
        for i in range(len(s)):
            if s[i] not in dictionary: #if open
                stack.append(s[i]) 
            elif s[i] in dictionary: #if its closed
                if len(stack) == 0: #a closed brace with no open is invalid
                    return False
                if stack[-1] != dictionary[s[i]]: #it should be immediately matched with its opener
                    return False
                stack.pop(-1) #free the pair
        return not stack #bool for empty stack or not-if someone leftover invalid
