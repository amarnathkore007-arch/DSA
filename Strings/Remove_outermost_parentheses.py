class solution:
    def removeouter(self,s):
        ans=[]
        depth=0
        for ch in s:
            if ch=="(":
                if depth>0:
                    ans.append(ch)
                depth+=1
            else:
                depth-=1
                if depth >0:
                    ans.append(ch)
        return "".join(ans)

# Function call
obj = solution()
s = "(()())(())"
result = obj.removeouter(s)
print(result)

