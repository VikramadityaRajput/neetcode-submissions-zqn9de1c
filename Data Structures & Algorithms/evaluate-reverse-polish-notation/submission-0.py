class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        #lambda functions
        operations = {"+" : lambda a, b: a + b, "*" : lambda a, b: a * b, "-" : lambda a, b: a - b, "/" : lambda a, b: int(a / b)}
        for token in tokens:
            if token in operations:
                b = stack.pop()
                a = stack.pop() #pops them and save value
                stack.append(operations[token](a, b))
            else:
                stack.append(int(token))
        return stack[0]


            