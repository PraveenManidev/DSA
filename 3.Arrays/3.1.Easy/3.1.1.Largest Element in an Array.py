n = int(input("Enter total number of elements"))

arr = list(map(int,input(f'Enter {n} number based on space split ').split()[:n]))
#arr = [1,2,3,4,5,9,7,5,15]
largest = arr[0]
for i in range(len(arr)):
    if(arr[i]>largest):
        largest = arr[i]
print(largest)

#Time complexity (O[n])