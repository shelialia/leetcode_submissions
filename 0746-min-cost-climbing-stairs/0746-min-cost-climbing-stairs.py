class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[len(cost)]
"""
cost = [10, 15, 20]
Choose to start at 15 
0 + 15 = 15 climb 2 stairs to reach top
Choose to start at 10
0 + 10 + 20 = 35 (Worse)

dp[i] = lowest cost to reach that index of the stair
dp[0], dp[1] = 0, 0 (can start from either index 0 or index 1)
dp[i] = to get to index i, lowest cost to reach i - 1 + cost[i - 1] 
OR lowest cost to reach i - 2 + cost[i - 2]

"""