#Always takes an element and places it in its correct position
def insertion_sort(arr,n):
    for i in range(0,n):
        j=i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    print(arr)

n = int(input('Enter total number'))
arr = list(map(int,input(f'Enter {n} number in space separated numbers').split()[:n]))
print(arr)
insertion_sort(arr,n)


#Time complexity - O(n^2) //Worst; O(n) - Best
