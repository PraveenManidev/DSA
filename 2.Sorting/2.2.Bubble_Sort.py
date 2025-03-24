#Bubble Sort = Push the maximum to the last by adjacent swapping
def bubble_sort(arr,n):
    for i in range(n-1,1,-1):
        for j in range(0,i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)
n = int(input("Enter total numbers"))
arr = list(map(int,input(f"Enter {n} numbers").split()[:n]))
print(arr)

bubble_sort(arr,n)

#Worst case = O[n^2] Best Case = O[n] @Sorted List