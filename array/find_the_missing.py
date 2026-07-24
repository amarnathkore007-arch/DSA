class solution:
    def missingno(self,nums):
        n=len(nums)
        expected_sum=n*(n+1)//2
        actual_sum=sum(nums)
        return expected_sum - actual_sum
obj=solution()
nums = [0,1,3,4,5]
print(obj.missingno(nums))