N = 121

original = N
reverse = 0

while N > 0:
    digit = N % 10
    reverse = reverse * 10 + digit
    N //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")