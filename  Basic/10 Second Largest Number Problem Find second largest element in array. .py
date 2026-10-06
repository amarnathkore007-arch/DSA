class Solution:
    def secondLargestElement(self, nums):
        if len(nums) < 2:
            return -1

        largest = float('-inf')
        second = float('-inf')

        for num in nums:
            if num > largest:
                second = largest
                largest = num
            elif num > second and num != largest:
                second = num

        return second if second != float('-inf') else -1
    
nums=[22,3,45,66,77,22,3]
s=Solution()
print(s.secondLargestElement(nums))