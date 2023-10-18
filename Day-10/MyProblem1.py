n=int(input())
l=[]
while(n>0):
    last=n%10
    l.append(last)
    n=n//10
l1=[0 for i in range(len(l))]
j=0
for i in range(len(l)-1,-1, -1):
    l1[j]=l[i]
    j+=1
l2=[]
for i in range(len(l1)):
    if(i%2!=0):
        l2.append(l1[i])
l3=[]
for i in l2:
    l3.append(i*i)
res=""
for i in range(len(l3)):
    res+=str(l3[i])
    if(len(res) == 4):
        break
print(res)
    
