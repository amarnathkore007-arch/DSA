N = 7
flag = True 
for i in range(2, N):
    if N % i == 0:
        flag = False
        break
if flag:
    print("Prime")
else:
    print("Not Prime")