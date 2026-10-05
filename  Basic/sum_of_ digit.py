N = 1234
sum_of_digits = 0
while N > 0:
    sum_of_digits += N % 10
    N //= 10
print("Sum of digits:", sum_of_digits)