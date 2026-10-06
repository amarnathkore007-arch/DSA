arr = [10, 25, 7, 45, 32]

largest = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print("Largest:", largest)