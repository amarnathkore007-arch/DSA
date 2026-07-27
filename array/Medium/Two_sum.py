#array is not sorted'

class solution:
    def twosum(self,nums,target):
        hashmap={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[nums[i]]=i
nums=[1,4,2,5,6]
target = 7

s = solution()
indices, values = s.twosum(nums, target)

print("Indices:", indices)
print("Values:", values)


#array is sorted
class Solution:
    def twoSum(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left < right:
            s = nums[left] + nums[right]

            if s == target:
                return [left, right], [nums[left], nums[right]]
            elif s < target:
                left += 1
            else:
                right -= 1

nums = [1, 2, 3, 4, 5, 6]
target = 7

s = Solution()
indices, values = s.twoSum(nums, target)

print("Indices:", indices)
print("Values:", values)