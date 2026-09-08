class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


"""       
coins = [1,2,5], amount = 11
11 = 5 + 5 + 1

coins = [2], amount = 3
-1

Naive solution (does not always work)
1. Sort by coins value descending
2. Loop through the coins, find out the max number of each coin you can use to form target (target//coin value). get the remainder after using each coin, then repeat. Add up all required coins, or return -1 if unable to find target value

Edge case: 
coins = [1, 3, 4]
amount = 6
Naive solution outputs 3 (4 + 1 + 1) but best solution is 2 (3 + 3)

Time complexity: O(n)

DP solution:
dp[i] = fewest number of coins needed to make up the amount
dp = [float('inf)] * target + 1
dp[0] = 0
for i in range(target + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i - coin] + 1, dp[i])

Time complexity: O(nm)
Space complexity: O(m)
"""

