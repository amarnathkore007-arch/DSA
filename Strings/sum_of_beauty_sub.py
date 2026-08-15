class Solution:

    def beautySum(self, s):

        ans = 0

        for i in range(len(s)):

            freq = [0] * 26

            for j in range(i, len(s)):

                index = ord(s[j]) - ord('a')
                freq[index] += 1

                maximum = 0
                minimum = float('inf')

                for f in freq:
                    if f > 0:
                        maximum = max(maximum, f)
                        minimum = min(minimum, f)

                ans += (maximum - minimum)

        return ans


obj = Solution()

s = "aabcb"

print(obj.beautySum(s))