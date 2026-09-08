class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

"""
n = 1
Output = 1

n = 2
Output = 2 
1 1
2

n = 3
Output = 3
1 1 1
2 1
1 2

n = 4 
Output = (n = 2) + (n = 3) = 5
1 1 2
2 2
1 1 1 1
2 1 1
1 2 1
"""