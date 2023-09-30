s=input()
l=[int(x) for x in s.split(" ")]
l1=[]
for x in l:
    if x>=0:
        l1.append(x)
l1.sort()
for i in range(0,len(s)):
    if(i!=l1[i]):
        print(i)
        break
print(max(l1)+1)

    
