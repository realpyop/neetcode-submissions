class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort array, so that we can use two pointer method
        nums.sort()
        res = []

        # Loop through every value
        for index, value in enumerate(nums):
            # Delete dupplicate by skipping them
            if index > 0 and value == nums[index - 1]:
                continue

            # Two pointer, solve it like two sum
            left, right = index + 1, len(nums) - 1
            while left < right:
                total = value + nums[left] + nums[right]
                if total == 0:
                    res.append([value, nums[left], nums[right]])
                    # Remove dupp
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
        return res


# Time: O(n^2)  -   Have to go through every elemnt twice because it can count toward a res array
# Space: O(1)   -   Using two point is constant space, if sorting doesn't count space and res array doesn't count toward run time

