def rotateArray(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = temp 

    return arr

n = int(input('Enter the total number of elements'))
arr = list(map(int,input(f'Enter the {n} number of space split numbers').split()[:n]))

print(rotateArray(arr))