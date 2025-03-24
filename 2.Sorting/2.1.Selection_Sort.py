#Selection sort = Select min & Swapping
def selection_sort(arr,n):
    for i in range(0,n-1):
        min = i
        for j in range(i+1,n):
            if(arr[j]<arr[min]):
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    print(arr)

n = int(input("Enter total numbers"))

arr = list(map(int,input(f'Enter the {n} space separated numbers').split()[:n]))

selection_sort(arr,n)


#Time complexity - O(n^2) //Best,Worst,Average