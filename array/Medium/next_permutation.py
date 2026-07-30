class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index = -1

        # Step 1: Find the pivot
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break

        # Step 2: If no pivot, reverse the array
        if index == -1:
            nums.reverse()
            return

        # Step 3: Find the next greater element and swap
        for i in range(len(nums) - 1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break

        # Step 4: Reverse the suffix
        nums[index + 1:] = reversed(nums[index + 1:])