class Solution:

    def bubble(self, nums):

        n = len(nums)

        for i in range(n):

            swapped = False

            for j in range(0, n - i - 1):

                if nums[j] > nums[j + 1]:

                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

                    swapped = True

            if not swapped:
                break

        return nums


arr = [5, 3, 8, 4, 2]

obj = Solution()              # Create object
result = obj.bubble(arr)      # Call function using object

print(result)