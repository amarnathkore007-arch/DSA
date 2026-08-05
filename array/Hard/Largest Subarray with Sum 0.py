class Solution:
    def maxLen(self, arr):
        prefixSum = 0
        maxLen = 0
        mp = {}

        for i in range(len(arr)):
            prefixSum += arr[i]

            # Subarray starts from index 0
            if prefixSum == 0:
                maxLen = i + 1

            # Prefix sum seen before
            elif prefixSum in mp:
                maxLen = max(maxLen, i - mp[prefixSum])

            # Store first occurrence only
            else:
                mp[prefixSum] = i

        return maxLen