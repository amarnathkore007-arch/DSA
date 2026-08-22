'''class solution:
    def xor(self,nums):
        result=0
        for num in nums:
            result^=num
        return result
'''
class Solution:

    def count_subarrays(self, nums, k):
        xor=0
        count=0
        frq={0:1}
        for num in nums:
            xor^=num
            need= xor ^ k
            if need in frq:
                count+=frq[need]
            frq[xor]=frq.get(xor,0)+1
        return count

obj = Solution()

nums = [4, 2, 2, 6, 4]
k = 6

print(obj.count_subarrays(nums, k))