class Solution:
    def isValid(self, s: str) -> bool:
        #create a dictionary for openers and closers
        #create stack to track openers
        #iterate through string
        #   if opener, add to stack
        #   if closer, pop from stack and check that opener and closer corresponds
        #       if not, return False
        #       if yes, continue
        #when loop ends, check if stack is empty
        #   if not empty, return False
        
        parens = {')':'(', '}':'{', ']':'['}
        openers = {'(', '[', '{'}
        parens_stack = []
        
        for char in s:
            if char in openers:
                parens_stack.append(char)
            else:
                if not parens_stack:
                    return False
                elif parens[char] == parens_stack[-1]:
                    parens_stack.pop()
                else:
                    return False
        return parens_stack == []
        