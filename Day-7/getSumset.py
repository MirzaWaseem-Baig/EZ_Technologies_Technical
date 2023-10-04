def backtrack(l,l2,n,target):
    if target == 0:
        return n,l2
    if l[n-1]>target:
        return n-1,backtrack(l,l2,n-1,target)
    return n-1,backtrack(l,l2,n-1,target) or n-1,backtrack(l,l2.append(l[n-1]),n-1,target-l[n-1])
def getsubset(l,l1,n,target):
    if n==0:
        return l1
    l2=[]
    l3=[]
    n,l3=backtrack(l,l2,n,target)
    l1.append(l3)
    return getsubset(l,l1,n,target)
l=list(map(int,input().split()))
n=len(l)
target=int(input())
l1=[[]]
print(getsubset(l,l1,n,target))