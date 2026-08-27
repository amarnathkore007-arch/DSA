class Solution:
    def findMin(self, nums):
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                # Minimum is in the right half
                low = mid + 1
            else:
                # Minimum is at mid or in the left half
                high = mid

        return nums[low]


# Call the function
nums = [4, 5, 6, 7, 0, 1, 2]

obj = Solution()
result = obj.findMin(nums)

print(result)