class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = prices[0]
        for price in prices[1:]:
            curr_profit = price - lowest_price
            max_profit = max(max_profit, curr_profit)
            lowest_price = min(lowest_price, price)
        return max_profit        