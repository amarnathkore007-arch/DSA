class Solution:
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False

        return goal in (s + s)


obj = Solution()

s = "abcde"
goal = "cdeab"

result = obj.rotateString(s, goal)
print(result)