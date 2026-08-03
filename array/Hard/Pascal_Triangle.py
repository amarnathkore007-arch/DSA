#Generate Entire Triangle

class Solution:
    def generate(self,numsrow):
        triangle=[]
        for i in range(len(numsrow)):
            row=[1]*(i+1)
            for j in range(1,i):
                row[j]=triangle[i-1][j-1]+triangle[i-1][j]
            triangle.append()
        return triangle    



#Return Nth row
class Solution:
    def getrow(self,rowindex):
        row=[1]
        ans=1
        for i in range(1,rowindex+1):
            ans=ans*(rowindex-i+1)//i
            row.append(ans)
        return row



#Find one element

def nCr(n, r):
    ans = 1

    for i in range(r):
        ans = ans * (n - i)
        ans = ans // (i + 1)

    return ans


def pascalElement(row, col):
    return nCr(row - 1, col - 1)


print(pascalElement(5, 3))   # Output: 6