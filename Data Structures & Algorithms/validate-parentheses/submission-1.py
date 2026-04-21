class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }
        for i in range(len(s)):
            if s[i] in ["{","(","["]:
                stack.append(s[i])
            elif s[i] in ["}",")","]"]:
                if not stack:
                    return False
                val = stack.pop()
                if (mp.get(val) != s[i]):
                    return False
        
        if stack:
            return False
        return True
                