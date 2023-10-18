s=input()
l=list(s.split(','))
op=""
for i in l:
    parts=i.split(":")
    key,value=parts
    max=0
    for i in value:
        if int(i)>max and int(i)<=len(key):
            max=int(i)
    if max == 0:
        op+='X'
    else:
        op+=key[max-1]
print(op)