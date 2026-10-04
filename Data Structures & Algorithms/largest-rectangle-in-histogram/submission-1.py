class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Have a stack that append pair(index, height)
        # Pop when top of stack height > currentHeight
        # MAKE SURE PUSH START INDEX UPDATE because we can push it back
        # since top of stack is > curr, their index can be the start index

        maxArea = 0
        stack = []

        for idx, height in enumerate(heights):
            start = idx
            # Pop condition
            while stack and stack[-1][1] > height:
                stackIdx, stackHeight = stack.pop()
                maxArea = max(maxArea, stackHeight * (idx - stackIdx))
                start = stackIdx
            stack.append((start, height))
        
        # When stack still not empty
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea