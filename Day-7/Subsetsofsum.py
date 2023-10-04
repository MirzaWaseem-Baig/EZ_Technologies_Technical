def find_subsets_with_sum(arr, target):
    def backtrack(start, target, path):
        if target == 0:
            subsets.append(path)
            return
        for i in range(start, len(arr)):
            if arr[i] <= target:
                backtrack(i + 1, target - arr[i], path + [arr[i]])
    subsets = []
    backtrack(0, target, [])
    return subsets
arr = list(map(int,input().split()))
target = int(input())
result = find_subsets_with_sum(arr, target)
print(result)
