n = int(input('Enter the number of elements'))

arr = list(map(int,input(f'Enter {n} space split elements in numbers').split()[:n]))
isSorted = True
for i in range(1,len(arr)):
    if(arr[i]<arr[i-1]):
        isSorted = False
        break
    
if(isSorted):
    print("Sorted Array")
else:
    print("Not Sorted Array")