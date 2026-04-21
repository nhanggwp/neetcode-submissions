class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_filtered = "".join(c.lower() for c in s if c.isalnum())
        return s_filtered == s_filtered[::-1]