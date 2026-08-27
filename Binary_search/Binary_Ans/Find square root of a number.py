class Solution:
    def floorSqrt(self, n):
        low = 1
        high = n
        answer = 0

        while low <= high:
            mid = (low + high) // 2

            if mid * mid <= n:
                # mid can be the answer
                answer = mid
                low = mid + 1
            else:
                # mid is too big
                high = mid - 1

        return answer


# Function call
solution = Solution()

print(solution.floorSqrt(36))
print(solution.floorSqrt(28))