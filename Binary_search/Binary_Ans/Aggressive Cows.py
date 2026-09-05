def aggressiveCows(nums, k):
    nums.sort()

    low = 1
    high = nums[-1] - nums[0]
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        if canPlace(nums, k, mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans


def canPlace(nums, k, distance):
    cows = 1
    last = nums[0]

    for i in range(1, len(nums)):

        if nums[i] - last >= distance:
            cows += 1
            last = nums[i]

        if cows == k:
            return True

    return False


nums = [0, 3, 4, 7, 10, 9]
k = 4

print(aggressiveCows(nums, k))