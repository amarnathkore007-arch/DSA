class Solution:
    def smallestDivisor(self, nums, threshold):

        low = 1
        high = max(nums)

        while low <= high:

            divisor = (low + high) // 2

            total = 0

            # Divide every number by divisor
            for num in nums:
                total += (num + divisor - 1) // divisor

            if total <= threshold:
                # divisor works
                # Try a smaller divisor
                high = divisor - 1
            else:
                # divisor is too small
                # Try a bigger divisor
                low = divisor + 1

        return low


# Function call
nums = [1, 2, 5, 9]
threshold = 6

obj = Solution()

answer = obj.smallestDivisor(nums, threshold)

print(answer)