def count(n):
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count
n = 123
print(count(n))



def revnumber(n):
    rev=0
    while n>0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n//10
    return rev
n=123
print(revnumber(n))




def printno(n):
    if n<=0:
        return
    printno(n-1)
    print(n)
printno(3)