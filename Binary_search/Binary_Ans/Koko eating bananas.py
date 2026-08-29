class Solution:
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)

        while low <= high:
            k = (low + high) // 2

            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k

            if hours <= h:
                high = k - 1
            else:
                low = k + 1

        return low


# Function call
piles = [3, 6, 7, 11]
h = 8

obj = Solution()

answer = obj.minEatingSpeed(piles, h)

print(answer)