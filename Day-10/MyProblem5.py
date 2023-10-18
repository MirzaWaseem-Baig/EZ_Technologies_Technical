arr=list(map(int,input().split()))
target=int(input())
j=len(arr)-1
for i in range(len(arr)):
    if(arr[i]+arr[j]>target):
        j-=1
    elif(arr[i]+arr[j]==target):
        print(i+1,j+1)
        
''' Ceil of number = smallest element but which is greater than that number '''
''' floor of number = greater element but which is smaller than that number '''