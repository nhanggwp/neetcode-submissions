class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for i in nums:
            d[i] = d.get(i,0) + 1
        
        for v in d.values():
            if v > 1:
                return True
        
        return False