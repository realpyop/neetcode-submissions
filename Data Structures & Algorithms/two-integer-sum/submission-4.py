class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in indices:
                return [indices[diff], index]
            indices[value] = index
        
        return [-1, -1]
