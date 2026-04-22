class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost = [0]* len(cost)
        mincost[0] = cost[0]
        mincost[1] = cost[1]
        for i in range(2,len(cost)):
            cost_1 = mincost[i-1] + cost[i]
            cost_2 = mincost[i-2] + cost[i]
            mincost[i] = min(cost_1,cost_2)
        
        return min(mincost[len(cost) -1],mincost[len(cost) -2])