class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Using a set to check if the number less by 1 exist
        numSet = set(nums)
        longest = 0
        for num in numSet:
            # If num - 1 no in set then it is the smaller number
            #   meaning we can start adding up from there
            if num - 1 not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

# Time: O(n)    -   n = size of the input array, could go through every element in the input
# Space: O(n)   -   n = size of the input array, set contain all unique element from input