class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Distance between left and right is the width, and height go for tallest
        # Increase the height as you move in since width is getting smaller
        left, right = 0, len(heights) - 1
        res = 0
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            res = max(res, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return res

# Time: O(n)    -   n = size of the input array since we could go through every value 
# Space: O(1)   -   constant size because we only use two poitner