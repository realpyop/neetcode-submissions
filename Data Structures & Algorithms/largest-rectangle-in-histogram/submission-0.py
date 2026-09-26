class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                stackIdx, stackHeight = stack.pop()
                maxArea = max(maxArea, (stackHeight * (i - stackIdx)))
                start = stackIdx    # cause height is taller, so we can extend width back
            stack.append((start, h))
        
        # When stack still not empty
        for i, h in stack:
            maxArea = max(maxArea, (h * (len(heights) - i)))
        
        return maxArea