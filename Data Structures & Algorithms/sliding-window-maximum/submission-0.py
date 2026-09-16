class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Using a monotonic decreasing queue in order to find the max
        output = []
        q = collections.deque()
        l, r = 0, 0

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop() 
            q.append(r)

            # Remove left val from window
            if l > q[0]:
                q.popleft()

            # Make sure window is size k
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1
        
        return output