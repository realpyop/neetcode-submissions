class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window, keep track on new character insdie window with a frequency map
        # (valid window) -> windowSize - max(count.values()) <= k
        # because we want to replace the least frequent value in the window but has to be <= k

        l, r = 0, 0
        res = 0
        count = {}

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            if ((r - l + 1) - max(count.values()) > k):
                count[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))
            r += 1

        return res