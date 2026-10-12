
arr = list(map(int, input("Enter elements: ").split()))

n = len(arr) + 1

total = n * (n + 1) // 2

arr_sum = 0
for i in arr:
    arr_sum += i

missing = total - arr_sum

print(missing)
