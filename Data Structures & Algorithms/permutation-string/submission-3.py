class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Hashmap of s1 and s2 (or frequency map like group anagram problem)
        # Have a match variable, if match == 26, that mean that there are s1 inside of s2
        # Else, keep shifting window and adding or subtracting values from hashmap(s2)
        
        # Edge case:
        if len(s1) > len(s2):
            return False

        s1_hashmap = {}
        s2_hashmap = {}
        for i in range(len(s1)):
            s1_hashmap[s1[i]] = 1 + s1_hashmap.get(s1[i], 0)
            s2_hashmap[s2[i]] = 1 + s2_hashmap.get(s2[i], 0)
        
        left, right = 0, len(s1)
        while right < len(s2):
            if s1_hashmap == s2_hashmap:
                return True
            
            # Adding character from right window
            if s2[right] not in s2_hashmap:
                s2_hashmap[s2[right]] = 0
            s2_hashmap[s2[right]] += 1

            # Moving left forward
            s2_hashmap[s2[left]] -= 1
            if s2_hashmap[s2[left]] == 0:
                del s2_hashmap[s2[left]]
            left += 1

            right += 1
        
        return s1_hashmap == s2_hashmap
    