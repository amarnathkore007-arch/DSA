class Solution:
    def rearrangeArray(self, nums):
        ans = [0] * len(nums)

        positive = 0
        negative = 1

        for num in nums:
            if num > 0:
                ans[positive] = num
                positive += 2
            else:
                ans[negative] = num
                negative += 2

        return ans