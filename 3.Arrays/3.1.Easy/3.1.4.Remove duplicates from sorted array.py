def remove_duplicate(arr):
    i = 0
    for j in range(1,len(arr)):
        if(arr[i]!=arr[j]):
            i+=1
            arr[i]=arr[j]
    return i+1


n = int(input('Enter the total number'))
arr = list(map(int,input(f'Enter {n} number of space split numbers').split()[:n]))

new_length = remove_duplicate(arr)
print(new_length)
print(arr[:new_length])