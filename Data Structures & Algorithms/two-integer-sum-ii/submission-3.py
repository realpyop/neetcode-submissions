class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Since this array is sorted, we can use two pointer, and move right 
        # if total is greater than target, left otherwise
        left, right = 0, len(numbers) - 1
        while left <= right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            elif total > target:
                right -= 1
            elif total < target:
                left += 1
        
        return [-1, -1]

#Time: O(n)     -   n = size of the input array, have to go through every elements
#Space: O(1)    -   Constant space because we're using two pointers, no extra space needed