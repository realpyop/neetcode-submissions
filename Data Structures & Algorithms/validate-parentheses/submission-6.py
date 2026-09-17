class Solution:
    def isValid(self, s: str) -> bool:
        # Using a stack and keep adding open parentheses to stack and pop when see a close
        stack = []
        closeToOpen = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        
        