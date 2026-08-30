class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # Build a prefix product
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
        
        # Looping backward to build postfix and res array
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = post * res[i]
            post = post * nums[i]
        
        return res