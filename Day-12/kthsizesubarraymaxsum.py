arr=list(map(int, input().split()))
k=int(input())
i,j=0,k-1
sum,summax=0,0
while(j<len(arr)):
    sum=arr[i]+arr[i+1]+arr[i+2]
    if(summax < sum):
        summax = sum
    i+=1
    j+=1
print(summax)