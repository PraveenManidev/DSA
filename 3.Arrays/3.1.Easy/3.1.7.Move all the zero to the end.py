def zero(arr):
    i = 0               # i will always be at '0' 
    for j in range(len(arr)):
        if(arr[j]!=0):
            arr[i],arr[j]=arr[j],arr[i]
            i+=1

n = int(input('Enter the total numbers'))
arr = list(map(int,input(f'Enter the {n} space based split numbers').split()[:n]))

zero(arr)
print(arr)