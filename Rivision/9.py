class Solution:
    def maximumProfit(self, arr):
        min_price = arr[0]
        max_profit = 0

        for price in arr:
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)

        return max_profit



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count:
                return False

            count[ch] -= 1

            if count[ch] < 0:
                return False

        return True

obj = Solution()

s = "abcde"
t = "cdeab"

result = obj.isAnagram(s, t)
print(result)