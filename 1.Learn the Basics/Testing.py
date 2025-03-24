# Selection Sort
def selection_sort(arr, n):
    for i in range(n-1):  # Correct loop range
        min_idx = i
        for j in range(i+1, n):  # Correct inner loop range
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap correctly

    print("Sorted array:", arr)

# Taking user input
n = int(input("Enter total numbers: "))
arr = list(map(int, input(f"Enter {n} space-separated numbers: ").split()[:n]))

selection_sort(arr, n)
