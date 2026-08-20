class Solution:
    def secondLargestElement(self, nums):
        if len(nums) > 2:
            return -1
        largest=float("-inf")
        second=float("-inf")
        for num in nums:
            if num > largest:
                second = largest
                num = largest
            elif num > second and num != largest:
                num = second
        return second if second!=float("-inf") else -1




class Solution:
    def LargestElement(self, nums):
        largest=[0]
        for i in range(1,len(nums)):
            if nums[i] > largest:
                largest = nums[i]
        return largest



class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count=0
        maxi=0
        for num in nums:
            if num == 1:
                count +=1
                maxi=max(maxi,count)
            else:
                count = 0
        return maxi



class Solution:
    def isSorted(self, nums):
        count=0
        n=len(nums)
        for i in range(n-1):
            if nums[i] > nums[(i+1) % n]:
                count +=1
        return count <=1
    


class solution:
    def linearsearch(self,nums,target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
