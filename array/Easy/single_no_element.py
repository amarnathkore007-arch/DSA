class Solution:
    # Function to find the single non-repeating element using XOR
    def getSingleElement(self, arr):
        xorr = 0

        # XOR all elements — duplicates cancel out
        for num in arr:
            xorr ^= num

        return xorr

# Driver code
arr = [4, 1, 2, 1, 2]
obj = Solution()
ans = obj.getSingleElement(arr)
print("The single element is:", ans)