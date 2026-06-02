class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += str(len(word)) + "#" + word
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j + 1 + length])
            i = j + 1 + length

        return res

# Note: Do it inplace with two point in decode code
# Time: O(n) -> total number accross the string
# Space: O(n) -> need to store all the string in the input array 

        