class Solution:
    def getFloorAndCeil(self, nums, x):
        low = 0
        high = len(nums) - 1

        floor = -1
        ceil = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == x:
                floor = nums[mid]
                ceil = nums[mid]
                return [floor, ceil]

            elif nums[mid] < x:
                floor = nums[mid]      # possible floor
                low = mid + 1          # search right

            else:
                ceil = nums[mid]       # possible ceil
                high = mid - 1         # search left

        return [floor, ceil]