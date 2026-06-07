class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Since the array is sorted, we can find the total of left and right, then
        #       move right if total is > target
        #       move left if total is < target
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
        
            if total == target:
                return [left + 1, right + 1]
        return [-1, -1]