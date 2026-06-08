class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets = [nums[i], nums[left], nums[right]]
                    res.add(tuple(triplets))
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        
        return [list(t) for t in res]

             