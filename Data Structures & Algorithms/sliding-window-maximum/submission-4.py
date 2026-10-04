class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Having a MONOTOIC DECREASING Q to keep highest value accessible from the left
        # Sliding window and update Q accordingly
        
        l, r = 0, 0
        res = []
        q = collections.deque()

        while r < len(nums):
            # Adding right value (keep highest value on top left)
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            # if l move pass top index, pop it from q
            if l > q[0]:
                q.popleft()

            # Update res and move window forward by doing something with l
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1

            r += 1
        
        return res