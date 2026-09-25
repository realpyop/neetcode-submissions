class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create an array of pairs
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        # Sort array in reserved order
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # Speed is faster than top of stack
                stack.pop()
            
        return len(stack)
