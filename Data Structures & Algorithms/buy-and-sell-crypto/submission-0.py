class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_num = float("inf")
        profit = 0
        for i in range(len(prices)):
            min_num = min(min_num, prices[i])
            profit = max((prices[i] - min_num),profit)
        
        return profit