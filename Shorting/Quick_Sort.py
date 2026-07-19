class Solution:
    def quickSort(self, nums, low, high):
        if low < high:
            pi = self.partition(nums, low, high)

            self.quickSort(nums, low, pi - 1)
            self.quickSort(nums, pi + 1, high)

        return nums

    def partition(self, nums, low, high):
        pivot = nums[high]
        i = low - 1

        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1
    
nums = [5, 2, 8, 1, 9, 3]
obj = Solution()
print(obj.quickSort(nums, 0, len(nums) - 1))