class solution :
    def largestelement(self , nums):
        largest = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > largest:
                largest = nums[i]
        return largest
nums=[-4 , -3, 0, 1, -8]
s=solution()
print(s.largestelement(nums))