def checksumset(arr,n,targetsum):
    if targetsum == 0:
        return True
    if n==0:
        return False
    if arr[n-1]>targetsum:
        return checksumset(arr,n-1,targetsum)
    
    return checksumset(arr,n-1,targetsum) or checksumset(arr,n-1,targetsum - arr[n-1])
l=list(map(int,input().split()))
n=len(l)
targetsum=int(input())
print(checksumset(l,n,targetsum))
       
    