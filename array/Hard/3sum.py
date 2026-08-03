class Solution:
    def threeSum(self, arr, n):
        # Step 1: Sort the array
        arr.sort()

        # Store the answer
        ans = []

        # Step 2: Fix one element
        for i in range(n):

            # Skip duplicate first elements
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            # Two pointers
            left = i + 1
            right = n - 1

            # Step 3: Find remaining two numbers
            while left < right:

                total = arr[i] + arr[left] + arr[right]

                if total == 0:
                    ans.append([arr[i], arr[left], arr[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left elements
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1

                    # Skip duplicate right elements
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return ans


# Driver Code
arr = [-1, 0, 1, 2, -1, -4]
obj = Solution()
print(obj.threeSum(arr, len(arr)))