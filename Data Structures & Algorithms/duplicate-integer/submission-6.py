class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for num in nums:
            if num in dup:
                return True
            dup.add(num)

        return False

# Time: O(n) -> Size of the input array
# Space: O(n) -> Set can grow as large as array if they're all unique