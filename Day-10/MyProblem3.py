s=input()
stack=[]
j=0
for i in s:
    if i in "({[":
        stack.append(i)
        j+=1
    elif i in ")}]":
        top=stack.pop()
        if(i == ')' and top != '(') or \
          (i == '}' and top != '{') or \
          (i == ']' and top != '['):
              print(j+1)
              break
        else:
            j+=1
if(len(stack)==0):
    print(0)
else:
    print(j+1)

       
        
        