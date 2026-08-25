class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a frequency dictionary 
        #   Key = array of size 26 for each character of the word
        #   Value = array contain word with the same frequency

        frequency = {}
        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord('a')] += 1
            if tuple(key) in frequency:
                frequency[tuple(key)].append(word)
            else:
                frequency[tuple(key)] = [word]
        
        return list(frequency.values())

# Time: O(m*n)  -   m = number of strings, n = size of the longest string
# Space: O(m)   -   m = number of strings
# Note: dictionary only take immutable object as key so turn key into tuple before operations