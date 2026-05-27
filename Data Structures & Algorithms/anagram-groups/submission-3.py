class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Build freq map 
        # Key: array of size 26, each index equal freq of letter of the word
        # Value: array of word that has the same freq of letter
        result = {}

        for word in strs:
            key = [0] * 26
            for letter in word:
                key[ord('a') - ord(letter)] += 1
            if tuple(key) in result:
                result[tuple(key)].append(word)
            else:
                result[tuple(key)] = [word]
        
        return list(result.values())

