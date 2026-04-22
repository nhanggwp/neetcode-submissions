class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        max_cost = [0] * n
        if n <= 2:
            temp_max = 0
            for i in range(n):
                temp_max = max(temp_max,nums[i])
                print(temp_max,nums[i])
            return temp_max

        max_cost[0] = nums[0]
        max_cost[1] = max(max_cost[0],nums[1])

        for i in range(2, len(nums)):
            max_cost[i] = max(max_cost[i-2] + nums[i], max_cost[i-1])

        return max_cost[len(nums) -1]           