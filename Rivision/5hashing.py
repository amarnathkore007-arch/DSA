class Solution:
    def twoSum(self, nums, target):
        hashmap={}
        for i in range(len(nums)):
            compilemnt=target-nums[i]
            if compilemnt in hashmap:
                return [hashmap[compilemnt],i]
            hashmap[nums[i]]=i