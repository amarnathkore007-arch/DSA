class Solution:
    def countOccurrences(self, arr, target):
        low = 0
        high = len(arr) - 1
        first = len(arr)

        # Lower Bound
        while low <= high:
            mid = (low + high) // 2

            if arr[mid] >= target:
                first = mid
                high = mid - 1
            else:
                low = mid + 1

        # Target not found
        if first == len(arr) or arr[first] != target:
            return 0

        low = 0
        high = len(arr) - 1
        last = len(arr)

        # Upper Bound
        while low <= high:
            mid = (low + high) // 2

            if arr[mid] > target:
                last = mid
                high = mid - 1
            else:
                low = mid + 1

        return last - first


# Call the function
arr = [0, 0, 1, 1, 1, 2, 3]
target = 1

obj = Solution()
result = obj.countOccurrences(arr, target)

print(result)