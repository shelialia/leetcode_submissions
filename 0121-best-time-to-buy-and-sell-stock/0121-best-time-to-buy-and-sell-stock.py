class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maximum_profit = 0
        for i in range(1, len(prices)):
            curr_profit = prices[i] - lowest
            maximum_profit = max(curr_profit, maximum_profit)
            if prices[i] < lowest:
                lowest = prices[i]
        return maximum_profit
        