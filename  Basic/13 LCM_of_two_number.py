a, b = map(int, input().split())

x = a
y = b

while y != 0:
    x, y = y, x % y

gcd = x

lcm = (a * b) // gcd

print(lcm)