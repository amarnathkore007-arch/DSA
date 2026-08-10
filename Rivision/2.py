class Solution:
    def selectionSort(self, nums):
        n=len(nums)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if nums[j]<nums[min_index]:
                    min_index=j
            nums[j],nums[min_index]=nums[min_index],nums[j]
        return nums
nums = [64, 25, 12, 22, 11]

obj = Solution()
print(obj.selectionSort(nums))


class Solution:
    def bubblesort(self, nums):
        n=len(nums)
        for i in range(n):
            swapped=False
            for j in range(0,n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
            if not swapped:
                break
        return nums


class Solution:
    def insertionsort(self, nums):
        n=len(nums)
        for i in range(n):
            key=[i]
            j=i-1
            while j>=0 and nums[j]>key:
                nums[j+1]=nums[j]
            nums[j+1]=key
        return nums


