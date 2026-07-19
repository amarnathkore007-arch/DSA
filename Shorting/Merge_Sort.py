class Solution:
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result
    

# Driver Code
nums = [38, 27, 43, 3, 9, 82, 10]

obj = Solution()
sorted_nums = obj.mergeSort(nums)
print("Sorted Array:", sorted_nums)
