class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        # 1) Generate a prefix
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        # 2) Loop backward to generate postfix
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = postfix * res[i]
            postfix *= nums[i]
        
        return res