class Solution:
    def maximumProfit(self, arr):
        min_price = arr[0]
        max_profit = 0

        for price in arr:
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)

        return max_profit