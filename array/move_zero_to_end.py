class solution:
    def movezeros(self,nums):
        i = 0

        for j in range(len(nums)):
            if nums[j] !=0:
                nums[i] , nums[j] = nums[j], nums[i]
                i +=1

obj=solution()
nums=[0,0,1,3,0,2,5,6,0,2]
obj.movezeros(nums)
print(nums)