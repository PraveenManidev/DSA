def union_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    result = []

    while i < len(arr1) and j < len(arr2):
        # Avoid duplicates in the result
        if i > 0 and arr1[i] == arr1[i - 1]:
            i += 1
            continue
        if j > 0 and arr2[j] == arr2[j - 1]:
            j += 1
            continue

