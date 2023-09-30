'''n=5
xor=0
for i in range(1,n+1):
    xor=xor^i
print(xor)'''
''' Big O(n) '''
''' For Big O(1): '''
''' n
    1 1
    2 3
    3 0
    4 4
    5 1
    6 7
    7 0
    8 8
    9 1'''
n=int(input())
if n%4==0:
    print(n)
elif n%4==1:
    print(1)
elif n%4==2:
    print(n+1)
elif n%4==3:
    print(0)

        