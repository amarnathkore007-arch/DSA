n=6
flag=True
for i in range(2,n):
    if n % i == 0:
        flag=False
        break
if flag:
    print("Prime")
else:
    print("Not prime")




n=10
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c


n=1234
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit