def reverse(arr, start, end):
    while(start<end):
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1


def rotateArrByD(arr,d):
    d = d % len(arr)
    n = len(arr)-1 

    reverse(arr,0,d-1) #Reverse till d
    reverse(arr,d,n)    # Reverse after d
    reverse(arr,0,n)    # Reverse complete arr


n = int(input('Enter the total number of elements'))
arr = list(map(int,input(f'Enter the {n} of elements space split numbers').split()[:n]))
d = int(input('Enter the d number'))

rotateArrByD(arr,d)
print(arr)