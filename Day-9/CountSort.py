def counting_sort(arr):
    if len(arr) == 0:
        return arr
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    count = [0] * range_val
    for num in arr:
        count[num - min_val] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    sorted_arr = [0] * len(arr)
    for num in arr[::-1]:
        sorted_arr[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
    return sorted_arr
arr = list(map(int,input().split()))
sorted_arr = counting_sort(arr)
print(sorted_arr)

