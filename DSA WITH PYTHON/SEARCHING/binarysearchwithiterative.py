# Iterative Binary Search Function

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2    #FLOOR DIVISION

        
        if arr[mid] < x:
            low = mid + 1

        
        elif arr[mid] > x:
            high = mid - 1

        
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


#  array ENTER THE SORTED ARRAY
arr =list(map(int,input("Enter the numbers with space in SORTED manner :: ").split()))
print(f"Your Array : {arr}")
x=int(input("Enter the target number :: "))

# Function call
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")