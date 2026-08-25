class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Build a frequency dictionary of each character in both string
        freq_s = {}
        for c in s:
            freq_s[c] = 1 + freq_s.get(c, 0)
        freq_t = {}
        for c in t:
            freq_t[c] = 1 + freq_t.get(c, 0)
        
        # Compare the dictionary
        return freq_s == freq_t
