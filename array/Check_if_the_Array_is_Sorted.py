class Solution:
    def isSorted(self, nums):
        #your code goes here
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1

        return count <= 1
# Function call
obj = Solution()

print(obj.isSorted([3,4,5,1,2]))   # True
print(obj.isSorted([1,2,3,4,5]))   # True
print(obj.isSorted([2,1,3,4]))     # False
print(obj.isSorted([1,1,1]))       # True

