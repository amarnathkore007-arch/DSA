class solution:
    def reverseword(self,s):
        words=s.split()
        words.reverse()
        return " ".join(words)
obj = solution()
s = "Amar kore"
result = obj.reverseword(s)
print(result)
