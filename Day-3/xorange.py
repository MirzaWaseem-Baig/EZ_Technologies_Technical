def xor1(n):
    if n%4==0:
        return n
    elif n%4==1:
        return 1
    elif n%4==2:
        return n+1
    elif n%4==3:
        return 0
l=int(input())
r=int(input())
print(xor1(r)^xor1(l-1))
