def is_pair_exist(arr,target):
    j=len(arr)-1
    for i in arr:
        if((i+arr[j])==target):
            return True
        else:
            j=j-1
    return False
arr=list(map(int, input().split()))
target=int(input())
print(is_pair_exist(arr,target))
    