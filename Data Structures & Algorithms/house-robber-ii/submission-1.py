class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_2(nums):
            n = len(nums)
            max_cost = [0] * n
            if n <= 2:
                temp_max = 0
                for i in range(n):
                    print(i)
                    temp_max = max(temp_max,nums[i])
                return temp_max

            max_cost[0] = nums[0]
            max_cost[1] = max(max_cost[0],nums[1])

            for i in range(2, len(nums)):

                max_cost[i] = max(max_cost[i-2] + nums[i], max_cost[i-1])

            print(max_cost)
            return max_cost[len(nums) -1] 
        n = len(nums)
        if(n == 0):
            return 0
        if (n == 1):
            return nums[0]
        return max(rob_2(nums[1:]),rob_2(nums[:-1]))        

        