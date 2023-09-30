s=input()
l=[int(x) for x in s.split(" ")]
for i in range(0,len(l)):
    if i not in l:
        print(i)
        break


    
