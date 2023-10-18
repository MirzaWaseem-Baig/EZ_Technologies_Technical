def sumfib(n):
    if(n<=2):
        return n-1
    return n + sumfib(n-1)
n=int(input())
print(n)
def fib(n):
    if(n<=2):
        return n-1
    else:
        return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))
        