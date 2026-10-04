class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # output = same length as input
        # Have a stack that append (temp, index) and pop when found higher temperature
        # number of day apart = i - stackIdx

        stack = []
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            # Pop condition
            while stack and temp > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                res[stackIdx] = idx - stackIdx
            stack.append((temp, idx))
        
        return res