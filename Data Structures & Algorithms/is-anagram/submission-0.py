class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_t = "".join(sorted(t))
        sorted_s = "".join(sorted(s))
        return sorted_t == sorted_s