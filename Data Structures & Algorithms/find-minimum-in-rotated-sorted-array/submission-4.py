class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search because array is sorted
        # when mid is found figure out which side of mid to search next
        
        l, r = 0, len(nums) - 1
        res = float("infinity")

        while l <= r:
            # Find mid
            mid = (l + r) // 2

            # Do something with mid
            res = min(res, nums[mid])

            # Update pointer
            if nums[l] > nums[r]:
                if nums[mid] > nums[r]: #smaller number on right side of mid
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                r = mid - 1
        
        return res