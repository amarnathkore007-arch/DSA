class Solution:
    def mejorityEle(self,nums):
        candidate= None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count +=1
            else:
                count -=1
        return candidate

nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
obj= Solution()
ans= obj.mejorityEle(nums)
print(ans)