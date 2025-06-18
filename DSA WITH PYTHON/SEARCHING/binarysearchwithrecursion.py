# Python  program for recursive binary search.

def binary_search(arr, low, high, x):

    
    if high >= low:

        mid = (high + low) // 2

       
        if arr[mid] == x:
            return mid

       
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1

#  array ENTER THE SORTED ARRAY
arr =list(map(int,input("Enter the numbers with space in SORTED manner :: ").split()))
print(f"Your Array : {arr}")
x=int(input("Enter the target number :: "))

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")