class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a difference dictionary, and subtract the value from target and keep the indices
        difference = {}
        for index, value in enumerate(nums):
            subtract = target - value
            if subtract in difference:
                return [difference[subtract], index]
            else:
                difference[value] = index
        
        return [-1, -1]

# Time: O(n)    -   n = the size of the input array since we could go on without finding it
# Space: O(n)   -   n = the size of the input array, the dictionary can be build on forever