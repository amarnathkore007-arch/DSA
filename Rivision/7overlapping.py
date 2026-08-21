class solution:
    def merge(self,intervals):
        intervals.sort()
        ans=[]
        for interval in intervals:
            if not ans or interval[0] > ans[-1][1]:
                ans.append(interval)
            else:
                ans[-1][1]=max(ans[-1][1],interval[1])
        return ans





# stock buy sell
class Solution:
    def maximumProfit(self, arr):
        min_price=arr[0]
        max_profit=0
        for price in arr:
            profit = price - min_price
            max_profit=max(max_profit,profit)
            min_price=min(min_price,price)
        return max_profit


