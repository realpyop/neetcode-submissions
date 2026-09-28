class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Having two condition for binary search
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[l] > nums[r]:
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                r = mid - 1
        
        return res