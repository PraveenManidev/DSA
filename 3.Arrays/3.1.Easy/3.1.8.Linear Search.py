def linear_search(arr,search):
    for i in range(len(arr)):
        if(arr[i]==search):
            return i 
    return -1
n = int(input('Enter the total number of elements'))
arr = list(map(int,input(f'Enter the {n} number of elements ').split()[:n]))
search = int(input('Enter the searching number'))
result = linear_search(arr,search)

print(result)