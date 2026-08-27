class Solution:
    def nthRoot(self, N, M):
        low = 1
        high = M

        while low <= high:
            mid = (low + high) // 2

            value = mid ** N

            if value == M:
                return mid

            elif value < M:
                # mid is too small
                low = mid + 1

            else:
                # mid is too large
                high = mid - 1

        return -1


# Function calls
solution = Solution()

print(solution.nthRoot(3, 27))
print(solution.nthRoot(4, 69))