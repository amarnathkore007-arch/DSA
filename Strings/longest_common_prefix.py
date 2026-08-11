class solution:
    def longprefix(self,str):
        prefix=""
        for i in range(len(str[0])):
            ch=str[0][i]
            for word in str:
                if i==len(word) or word[i]!=ch:
                    return prefix
            prefix +=ch
        return prefix

obj=solution()
str=["flow","flower","flight"]
result=obj.longprefix(str)
print(result)