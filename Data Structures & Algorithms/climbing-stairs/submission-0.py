class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climb_memo(n):
            if n in memo:
                return memo[n]
            
            if n == 1:
                return 1
            elif n == 2:
                return 2
            
            result = climb_memo(n-1) + climb_memo(n-2)
            memo[n] = result
            return result

        ans = climb_memo(n)
        return ans