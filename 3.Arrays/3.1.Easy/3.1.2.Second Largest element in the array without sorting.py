n = int(input('Enter the number of elements'))
arr = list(map(int,input(f'Enter {n} number of space based split').split()[:n]))

largest = arr[0]
second_largest = -1

for i in range(len(arr)):
    if (arr[i]>largest):
        second_largest = largest
        largest = arr[i]
    elif (arr[i] > second_largest and arr[i] < largest):
        second_largest = arr[i]
print(second_largest)