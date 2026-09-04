class Solution:
    def trap(self, height: List[int]) -> int:
        # Have two pointers one at the front and one at the end
        left, right = 0, len(height) - 1
        res = 0

        # keeping maxLeft and maxRight because the higher pillar from each side determien the ammount of water hold
        maxLeft, maxRight = height[left], height[right]

        # Loop until the pointer meet
        while left < right:
            # if left is shorter then start there, else right
            if height[left] <= height[right]:
                left += 1
                curr = maxLeft - height[left]
                # If < 0 (negative), add 0 to result
                if curr <= 0:
                    res += 0
                else:
                    res += curr
                maxLeft = max(maxLeft, height[left])
            else:
                right -= 1
                curr = maxRight - height[right]
                # If < 0 (negative), add 0 to result
                if curr <= 0:
                    res += 0
                else:
                    res += curr
                maxRight = max(maxRight, height[right])
        return res

# Time: O(n)    -   n = size of the input array
# Space: O(1)   -   we only use pointer and res variable to keep track of the result, no extra space needed 