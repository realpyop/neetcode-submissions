class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = []
        total = 0
        for num in nums:
            total += num
            self.preSum.append(total)

    def sumRange(self, left: int, right: int) -> int:
        rightPrefix = self.preSum[right]
        if left > 0:
            leftPrefix = self.preSum[left - 1]
        else:
            leftPrefix = 0
        return rightPrefix - leftPrefix


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)