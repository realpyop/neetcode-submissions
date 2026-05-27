class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in indices:
                return [indices[diff], index]
            indices[value] = index
        
        return [-1, -1]


# Time: O(n) -> Could go through the whole array without using it 
# Space: O(n) -> Could build a whole dictionary with the size of the array