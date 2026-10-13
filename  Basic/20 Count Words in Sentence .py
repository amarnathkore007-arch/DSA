n=121
orignal=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
if orignal==rev:
    print("palindo")
else:
    print("not")
