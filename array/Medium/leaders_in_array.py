class Solution:
    def leaders(self, nums):
        ans = []
        max_so_far = float('-inf')

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > max_so_far:
                ans.append(nums[i])
                max_so_far = nums[i]

        ans.reverse()
        return ans