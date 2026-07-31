class Solution:
    def longestConsecutive(self, nums):
        # If the array is empty
        if not nums:
            return 0

        # Store all numbers in a set for O(1) lookup
        num_set = set(nums)

        longest = 0

        # Traverse each unique number
        for num in num_set:

            # Check if it is the start of a sequence
            if num - 1 not in num_set:

                current = num
                length = 1

                # Count consecutive numbers
                while current + 1 in num_set:
                    current += 1
                    length += 1

                # Update the longest sequence length
                longest = max(longest, length)

        return longest


# Driver Code
if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]

    solution = Solution()
    ans = solution.longestConsecutive(nums)

    print("The longest consecutive sequence is:", ans)