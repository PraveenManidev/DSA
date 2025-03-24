def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as pivot
    i = low - 1  # Pointer for the smaller element
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than pivot
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot into correct position
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Partition index
        quicksort(arr, low, pi - 1)  # Recursively sort left partition
        quicksort(arr, pi + 1, high)  # Recursively sort right partition

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)