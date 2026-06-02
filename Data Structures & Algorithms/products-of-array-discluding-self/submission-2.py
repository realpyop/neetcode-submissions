class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res[i] = nums[0:i-1] * nums[i+1:]
        #             ^             ^
        #             |             |
        #           prefix        postfix

        res = [1] * len(nums)

        # 1) Build a prefix product
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # 2) Use on variable to keep postfix and build result array backward
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * postfix
            postfix *= nums[i]
    
        return res
        
        