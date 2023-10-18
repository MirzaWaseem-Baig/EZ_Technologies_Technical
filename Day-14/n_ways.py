def find_n_ways(n):
    if n == 1:
        return 1
    if n <= 0:
        return 0
    return find_n_ways(n-1)+find_n_ways(n-2)+find_n_ways(n-3)
print(find_n_ways(5))