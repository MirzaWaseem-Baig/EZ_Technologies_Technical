def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        inversion_count = 0 
        inversion_count += mergeSort(left_half)
        inversion_count += mergeSort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
                # If an element from the right half is smaller,
                # it's an inversion with all remaining elements in the left half
                inversion_count += len(left_half) - i
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        return inversion_count

    return 0
arr = list(map(int, input().split()))
inversions = mergeSort(arr)
print("Sorted array:", arr)
print("Number of inversions:", inversions)
