class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = [1] * n
        surfix_prod = [1] * n

        prefix_prod[0] = nums[0]
        for i in range(1,len(nums)):
            prefix_prod[i] = prefix_prod[i-1] * nums[i]

        surfix_prod[n-1] = nums[n-1]
        for i in range(n-2,-1, -1):
            surfix_prod[i] = surfix_prod[i+1] * nums[i]
           
    
        res = []
        res.append(surfix_prod[1])
        for i in range(1,n-1):
            results = surfix_prod[i+1] * prefix_prod[i-1]
            res.append(results)
        
        res.append(prefix_prod[n-2])

        return res
            
        