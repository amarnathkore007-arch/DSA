class Solution:
    def insertionSort(self, nums, n=None):
        if n is None:
            n = len(nums)

        # Base case
        if n <= 1:
            return nums

        # Recursively sort first n-1 elements
        self.insertionSort(nums, n - 1)

        # Insert last element at its correct position
        last = nums[n - 1]
        j = n - 2

        while j >= 0 and nums[j] > last:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = last
        return nums

# Driver Code
nums = [38, 27, 43, 3, 1, 82, 10]

obj = Solution()
sorted_nums = obj.insertionSort(nums)
print("Sorted Array:", sorted_nums)