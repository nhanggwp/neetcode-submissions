class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        des = 0

        if des == n -1:
            return True
        for i in range(n):
            if i > des:
                return False
            des = max(des, i + nums[i])
            if des >= n-1:
                return True
        
        return False


