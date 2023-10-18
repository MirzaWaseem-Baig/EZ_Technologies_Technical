def countSort(arr):
    arr1=[0 for x in range(len(arr))]
    res=[0 for x in range(len(arr))]
    for i in arr:
        arr1[i]+=1
    for i in range(len(arr)-1):
        arr1[i+1]=arr1[i]+arr1[i+1]
    for i in range((len(arr)-1),-1,-1):
        k=arr[i]
        arr1[k]-=1
        j=arr1[k]
        res[j]=k
    return res
arr=list(map(int,input().split()))
print(countSort(arr))
     