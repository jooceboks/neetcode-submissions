class Solution:
    def isValid(self, s: str) -> bool:
        openings = {'{' : '}', '[' :']', '(' : ')'}
        stack = []
        for char in s:
            if char in openings:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                recent = stack.pop()
                if openings[recent] != char:
                    return False

        if len(stack) == 0:
            return True       
        return False 
