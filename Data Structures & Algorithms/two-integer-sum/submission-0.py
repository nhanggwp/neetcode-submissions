class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            d[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d and d[diff] != i:
                return [i,d[diff]]
        
        return [0,0]