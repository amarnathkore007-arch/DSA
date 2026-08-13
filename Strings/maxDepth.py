class Solution:
    def maxDepth(self, s):
        depth=0
        maxdepth=0
        for ch in s:
            if ch=="(":
                depth +=1
                maxdepth=max(depth,maxdepth)
            elif ch==")":
                depth -=1
        return maxdepth
    
obj = Solution()

s = "(1+(2*3)+((8)/4))+1"

print(obj.maxDepth(s))