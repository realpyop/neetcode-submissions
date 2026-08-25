class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num)
        return False

# Time: O(n)  - n is the size of the input array
# Space: O(n) - n is the size of the input array, every number could be unique 