arr = [5, 8, 2, 10, 3]

largest = arr[0]
smallest = arr[0]

for num in arr:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)


