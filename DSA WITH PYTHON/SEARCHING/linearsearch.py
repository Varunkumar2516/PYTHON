def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

# Example
arr = list(map(int,input("Enter the numbers with space").split()))
print(f"Your Array : {arr}")
target=int(input("Enter the target number :: "))


result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array")