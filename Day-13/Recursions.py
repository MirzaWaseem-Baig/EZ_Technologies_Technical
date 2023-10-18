import time
start_time = time.time()
def fun(n):
    if n <=2 : return n
    return fun(n-2) + fun(n-4)
print(fun(16))
end_time = time.time()
execution_time = end_time - start_time
print(execution_time)