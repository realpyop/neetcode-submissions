class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case:
        if len(t) > len(s):
            return ""

        # Generate hashmap for t
        tCount, window = {}, {}
        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)
        
        # Start sliding window
        have, need = 0, len(tCount)
        res, resLen = [-1, -1], float("infinity")
        l, r = 0, 0
        while r < len(s):
            # adding character to our window hashmap
            character = s[r]
            window[character] = 1 + window.get(character, 0)

            # update our have variable
            if (character in tCount) and (window[character] == tCount[character]):
                have += 1
            
            # Popping character from the left
            while have == need:
                windowSize = r - l + 1
                if windowSize < resLen:
                    res = [l, r]
                    resLen = windowSize
                
                window[s[l]] -= 1
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
            r += 1

        # Generate result
        l, r = res
        return s[l:r+1] if resLen != float('infinity') else ""
