class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 Pointers 
        left, right = 0, len(heights) - 1
        res = 0

        # Loop
        while left < right:
            # height = shorter bar
            # width = distance between left and right 
            height = min(heights[left], heights[right])
            width = right - left
            area = height * width
            # Compare res
            res = max(area, res)

            # Move the shorter bar since we want to maximize area
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return res