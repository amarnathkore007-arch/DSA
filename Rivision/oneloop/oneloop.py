class solution :
    def largestelement(self , nums):
        largest=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>largest:
                largest=nums[i]
        return largest
nums=[-4 , -3, 0, 1, -8]
s=solution()
print(s.largestelement(nums))



class solution :
    def second(self , nums):
        largest=nums[0]
        secondlargest=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>largest:
                secondlargest=largest
                largest=nums[i]
            elif nums[i]>secondlargest and nums[i]!=largest:
                secondlargest=nums[i]
        return secondlargest
nums=[-4 , -3, 0, 1, -8]
s=solution()
print(s.second(nums))   


class solution :
    def findMaxConsecutiveOnes(self, nums):
        max_ones = 0
        current_ones = 0
        for n in nums:
            if n == 1:
                current_ones += 1
                max_ones = max(max_ones, current_ones)
            else:
                current_ones = 0
        return max_ones
obj = solution()
nums = [1, 1, 0, 1, 1, 1]
print(obj.findMaxConsecutiveOnes(nums))