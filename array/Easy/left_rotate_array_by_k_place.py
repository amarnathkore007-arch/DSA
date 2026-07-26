class soution:
    def rotatebykplace(self,nums,k) :
        n=len(nums)
        k =k%n
        temp=nums[:k]
        for i in range(k,n):
            nums[i-k]=nums[i]
        for i in range(k):
            nums[n-k+i] =temp[i]
