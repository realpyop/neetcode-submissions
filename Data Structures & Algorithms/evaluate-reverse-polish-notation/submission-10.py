class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Have a stack and append number onto the stack
        # When it hit an operators we pop till stack empty and use the number to do operation
        # Append the result back onto the stack
        stack = []
        operators = ("+", "-", "*", "/")
        for val in tokens:
            if val == "+":
                stack.append(int(stack.pop() + stack.pop()))
            elif val == "-":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(int(val2 - val1))
            elif val == "*":
                stack.append(int(stack.pop() * stack.pop()))
            elif val == "/":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(int(val2 / val1))
            else:
                stack.append(int(val))
        
        return stack[-1]