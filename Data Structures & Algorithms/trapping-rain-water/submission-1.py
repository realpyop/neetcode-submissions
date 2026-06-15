class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        # Using two pointer approach
        left, right = 0, len(height) - 1
        res = 0

        # General formula
            # 1) Find the minimum between maxLeft and maxRight 
            # 2) Subtract that minimum with the current height 
        maxLeft, maxRight = height[left], height[right]
        while left < right:
            # if maxLeft is smaller that mean we should compute from there since
            # lower level can stop the water from spilling
            if maxLeft <= maxRight:
                left += 1
                curr = maxLeft - height[left]
                if curr <= 0:
                    res += 0
                else:
                    res += curr
                maxLeft = max(maxLeft, height[left])
            else:
                right -= 1
                curr = maxRight - height[right]
                if curr <= 0:
                    res += 0
                else:
                    res += curr
                maxRight = max(maxRight, height[right])
        
        return res