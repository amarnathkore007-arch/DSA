class soution:
    def rotatebyone(self,nums):
        n=len(nums)
        if len(nums)==0:
            return
        temp=nums[0]
        for i in range(n-1):
            nums[i] = nums[i+1]

        nums[n-1] = temp

