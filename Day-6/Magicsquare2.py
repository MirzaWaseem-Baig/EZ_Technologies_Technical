n=int(input())
magicsquare=[[0 for x in range(n)] for y in range(n)]
i,j=0,n//2
num=1
while num<=n*n:
    magicsquare[i][j]=num
    num=num+1
    newi,newj=(i-1) % n,(j+1) % n
    if magicsquare[newi][newj]!=0:
        i=(i+1)%n
    else:
      i,j=newi,newj
for row in magicsquare:
    print(row)
    
