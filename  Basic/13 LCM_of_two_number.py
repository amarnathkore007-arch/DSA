a=int(input("A="))
b=int(input("B="))


x = a
y = b

while y != 0:
    x, y = y, x % y

gcd = x

lcm = (a * b) // gcd

print(lcm)