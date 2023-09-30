def findsingle(a):
    res=a[0]
    for i in range(1,len(a)):
        res=res^a[i]
    return res
s=input()
a=[int(x) for x in s.split(" ")]
print(findsingle(a))
