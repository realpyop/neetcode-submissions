class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge case: if the length are different then they're not anagram
        if len(s) != len(t):
            return False

        # Generate word frequency for S string
        freq_s = {}
        for char in s:
            freq_s[char] = 1 + freq_s.get(char, 0)
        
        # Generate wrod freqeuncy for T string
        freq_t = {}
        for char in t:
            freq_t[char] = 1 + freq_t.get(char, 0)
        
        # If same frequency then they're anagram
        return freq_s == freq_t


# Time: O(n) -> going through every char in the string
# Space: O(n) -> store every char in the string if they're all unique 

