class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        i = 0

        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1

nums = [0,0,3,3,5,6]

s = Solution()

k = s.removeDuplicates(nums)


print(nums)
print(nums[:k])