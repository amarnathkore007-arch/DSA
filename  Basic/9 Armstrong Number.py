N = 153

original = N
digits = len(str(N))
total = 0

while N > 0:
    digit = N % 10
    total += digit ** digits
    N = N // 10

if total == original:
    print("Armstrong")
else:
    print("Not Armstrong")