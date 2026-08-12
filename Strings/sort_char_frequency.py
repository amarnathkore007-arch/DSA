class Solution:
    def frequencySort(self, s):

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        sorted_chars = sorted(count.items(), key=lambda x: x[1], reverse=True)

        ans = ""

        for ch, freq in sorted_chars:
            ans += ch * freq

        return ans


obj = Solution()

s = "tree"

print(obj.frequencySort(s))