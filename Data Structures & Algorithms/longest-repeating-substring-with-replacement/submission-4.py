class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Have a frequency map of each character in the string
        # Start a sliding window from the beginning 
        # Check for valid condition 
            # (if size of window - max value <= k)
                # res = max(res, size of window)
            # Else
                # left += 1
                # count of character -= 1
        
        count = {}
        res = 0
        l, r = 0, 0

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        
        return res

# Time: O(26 * n)   -   because we need to go through all capital character to find max
# Space: O(n)       -   n = size of the input array, because every character could be unique   