class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Using two pointer to check from the front and back if they are the same
        left, right = 0, len(s) - 1
        while left <= right:
            # Removing space between left and right character
            while left < right and not self.isAlphaNumerical(s[right]):
                right -= 1
            while left < right and not self.isAlphaNumerical(s[left]):
                left += 1
            # Comparision step have to be done after removing space and non alphanumeric character
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
                
        return True
            

    # Helper function: check if character is alphanumeric 
    def isAlphaNumerical(self, c: str) -> bool:
        return ((ord("a") <= ord(c) <= ord("z")) or
                (ord("A") <= ord(c) <= ord("Z")) or
                (ord("0") <= ord(c) <= ord("9"))
        )

# Time: O(n)    -   n = size of input string
# Space: O(1)   -   no extra space needed only using two pointer


