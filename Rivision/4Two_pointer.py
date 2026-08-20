class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        i =0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i +=1
                nums[i]=nums[j]
        return i+1


class solution:
    def movezeros(self,nums):
        i =0
        for j in range(len(nums)):
            if nums[j] !=0:
                nums[i],nums[j]=nums[j],nums[i]
                i +=1



class Solution:
    def rearrangeArray(self, nums):
        ans=[0]*len(nums)
        positive=0
        negative=1
        for num in nums:
            if num > 0:
                ans[positive]=num
                positive +=2
            else:
                ans[negative]=num
                negative +=2
        return ans