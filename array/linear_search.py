class solution:
    def linearsearch(self,nums,target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
obj=solution()
nums=[2, 3, 5, 6, 2, 9]

print(obj.linearsearch(nums,5))