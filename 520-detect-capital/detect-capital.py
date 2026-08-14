class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Case 1: all uppercase
        if word.isupper():
            return True

        # Case 2: all lowercase
        if word.islower():
            return True

        # Case 3: first letter uppercase, rest lowercase
        if word[0].isupper() and word[1:].islower():
            return True

        return False