def primeadder(n):
    while n>0:
        last=n%10
        count =1
        s = 0
        for i in range(1,last):
            if(last % i == 0):
                count +=1
        if(count == 2):
            s = s + last
        n=n//10
    return s
n=int(input())
print(primeadder(n))