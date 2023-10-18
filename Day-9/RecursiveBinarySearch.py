def binary_search(arr, target,left,right):
    if left > right:
        return -1  
    mid = left + (right - left) // 2  
    if arr[mid] == target:
        return mid  
    elif arr[mid] < target:
        return binary_search(arr,target,mid+1,right)
    else:
        return binary_search(arr,target,left,mid-1)  
arr = list(map(int,input().split()))
target = int(input())
result = binary_search(arr, target,0,len(arr)-1)
if result != -1:
    print(f"Element {target} found")
else:
    print("Element not found in the array")

