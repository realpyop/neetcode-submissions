class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Have a left at 0 and right at the end, move them inward until they're not equal
        left, right = 0, len(s) - 1
        while left <= right:
            #remove "space" in between
            while left < right and not self.isAlphaNum(s[left]):
                left += 1
            while left < right and not self.isAlphaNum(s[right]):
                right -= 1
            # Comparition
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


    # Helper function to help see if the character is alphaNumeric
    def isAlphaNum(self, character):
        return ((ord("A") <= ord(character) <= ord("Z")) or
                (ord("a") <= ord(character) <= ord("z")) or
                (ord("0") <= ord(character) <= ord("9"))
        )