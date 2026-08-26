class Solution:
    def singleNonDuplicate(self, nums):
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            # Make mid even
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                # Pair is correct, single is on the right
                low = mid + 2
            else:
                # Pair is broken, single is here or on the left
                high = mid

        return nums[low] 
nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]

solution = Solution()
answer = solution.singleNonDuplicate(nums)

print(answer)