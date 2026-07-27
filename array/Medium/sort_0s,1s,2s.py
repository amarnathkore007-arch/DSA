class Solution:
    def sortZeroOneTwo(self, nums):

        # Three pointers
        low = 0                  # Position to place the next 0
        mid = 0                  # Current element being checked
        high = len(nums) - 1     # Position to place the next 2

        # Continue until all elements are checked
        while mid <= high:

            # If current element is 0
            if nums[mid] == 0:
                # Swap it to the front
                nums[low], nums[mid] = nums[mid], nums[low]

                # Move both pointers forward
                low += 1
                mid += 1

            # If current element is 1
            elif nums[mid] == 1:
                # 1 is already in the correct middle position
                mid += 1

            # If current element is 2
            else:
                # Swap it with the last unsorted element
                nums[mid], nums[high] = nums[high], nums[mid]

                # Move high backward
                high -= 1

                # Don't move mid because the new element
                # at mid has not been checked yet.


# Driver Code
nums = [2, 0, 2, 1, 1, 0]

obj = Solution()
obj.sortZeroOneTwo(nums)

print(nums)