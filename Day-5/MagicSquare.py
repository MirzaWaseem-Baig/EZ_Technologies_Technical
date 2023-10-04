n=int(input())
m=[[0 for x in range(n)] for y in range(n)]
k=1
i=0
j=n//2
while(k<=n*n):
    if(i==-1 and j==n):
        i=0
        j=n-2
    if(i==-1):
        i=n-1
    if(j==n):
        j=0
    if(m[i][j]):
        i=i+2
        j=j-1
    else:
        m[i][j]=k
        k=k+1
    j=j+1
    i=i-1
for row in m:
    print(m)
    
