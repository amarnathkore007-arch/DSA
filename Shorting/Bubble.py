class Solution:
    def bubbleSort(self, nums):
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
nums=[2,11,4,66,8,99]

obj=Solution()
print(obj.bubbleSort(nums))