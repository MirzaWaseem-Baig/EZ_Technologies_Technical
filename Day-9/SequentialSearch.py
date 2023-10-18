def SeqSearch(arr,target):
    for i in range(len(arr)):
        if(target == arr[i]):
            print("Element Found")
            return
    print("Element Not Found")
arr=list(map(int,input().split()))
target=int(input())
SeqSearch(arr,target)
