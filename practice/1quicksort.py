def quicksort(arr,start,end):
    if start>=end:
         return
      
    pivotindex=lomutopartition(arr,start,end)
    quicksort(arr,start,pivotindex-1)
    quicksort(arr,pivotindex+1,end)


def lomutopartition(arr,start,end):
     pivot=arr[end]
     i=start-1

     for j in range(start ,end):
          if arr[j]<=pivot:
               i=i+1
               arr[i],arr[j]=arr[j],arr[i]
     arr[i+1],arr[end]=arr[end],arr[i+1] 
     return i+1         


# DRIVERS CODE

n=int(input("ENter the size of array"))
arr =[]
print(f"Enter the {n} numbers:")
for i in range(n):
     num=int(input())
     arr.append(num)
print("given array",arr)
quicksort(arr,0,n-1) 
print("sorted array ",arr)