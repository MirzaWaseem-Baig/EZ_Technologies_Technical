arr=list(map(int, input().split()))
prefix_sum=[0 for i in range(len(n))]
for i in range(len(n)):
    if i == 0:
        prefix_sum[i] = arr[i]
    else:
        prefix_sum[i]=arr[i]+prefix_sum[i-1]
    for query in queries:
        i = query[0]
        j = query[1]
        if i == 0:
            print(prefix_sum[j], end=" ")
        else:
            print(prefix_sum[j] - prefix_sum[i-1], end=" ")
            