class Solution:
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)

        while low <= high:
            k = (low + high) // 2

            hours = 0

            # Calculate how many hours Koko needs
            for pile in piles:
                hours += (pile + k - 1) // k

            if hours <= h:
                # k is enough, try a smaller speed
                high = k - 1
            else:
                # k is too slow, increase speed
                low = k + 1

        return low