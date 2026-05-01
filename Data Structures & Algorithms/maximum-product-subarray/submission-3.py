class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maximum = nums[0]
        minimum = nums[0]
        max_check = maximum
        for i in range(1,n):
            old_max = maximum
            maximum = max((maximum * nums[i]), (minimum * nums[i]), nums[i])

            max_check = max(maximum,max_check)
            minimum = min((old_max * nums[i]), (minimum * nums[i]), nums[i])

        return max_check