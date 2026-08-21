class Solution:
    def threeSum(self, arr, n):
        arr.sort()
        ans=[]
        for i in range(n):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                total = arr[i]+arr[left]+arr[right]
                if total == 0:
                    ans.append([arr[i],arr[left],arr[right]])
                    left +=1
                    right -=1

                    while left < right and arr[left] == arr[left - 1]:
                        left +=1
                    while left < right and arr[right] == arr[right + 1]:
                        right -=1
                elif total < 0:
                    left +=1
                else:
                    right-=1
        return ans

arr = [-1, 0, 1, 2, -1, -4]
obj = Solution()
print(obj.threeSum(arr, len(arr)))








class Solution:
    def maxSubArray(self, nums):
        max_sum=nums[0]
        current_sum=0
        for num in nums:
            current_sum +=num
            if current_sum > max_sum:
                max_sum=current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum
    
# Driver Code
nums = [2, 3, 5, -2, 7, -4]

obj = Solution()
ans = obj.maxSubArray(nums)

print(ans)