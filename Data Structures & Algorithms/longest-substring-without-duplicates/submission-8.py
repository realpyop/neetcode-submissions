class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        longest = 0
        mySet = set()

        while right < len(s):
            while s[right] in mySet:
                mySet.remove(s[left])
                left += 1
            mySet.add(s[right])
            longest = max(longest, right - left + 1)
            right += 1

        return longest
                
