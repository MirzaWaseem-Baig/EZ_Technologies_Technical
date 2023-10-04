l=["(","[","{","}","]",")"]
stack=[]
if len(l)%2!=0:
    print(False)
for i in l:
    if(i=="(" or i=="[" or i=="{"):
        stack.append(i)
        print(stack)
    else:
        temp=stack.peek()
        if((temp=="(" and i == ")") or (temp == "[" and i == "]") or (temp == "{" and i == "}")):
            stack.pop()
        else:
            print(False)
print(len(l))
'''count
push
closing diff
opening not there

'''