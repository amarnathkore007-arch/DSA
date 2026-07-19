class Solution:
    def bubbleSort(self, nums, n=None):
        if n is None:
            n = len(nums)

        # Base case
        if n == 1:
            return nums

        # One pass of Bubble Sort
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        # Recursive call for remaining array
        return self.bubbleSort(nums, n - 1)
    

# Driver Code
nums = [38, 27, 43, 3, 1, 82, 10]

obj = Solution()
sorted_nums = obj.bubbleSort(nums)
print("Sorted Array:", sorted_nums)