n=input()
op=''
for i in range(1,len(n),2):
    op+=str(int(n[i])**2)
print(op[:4])