class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        f = nums[0]
        for x in nums[1:]:
            f = max(f,0) + x
            ans = max(f,ans)

        return ans    
                

            