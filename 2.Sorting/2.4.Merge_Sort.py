#Merge sort - Divide and Merge
def mergesort(arr):
    if(len(arr)<=1):
        return arr
    
    mid = len(arr) // 2

    left_half = mergesort(arr[:mid]) 
    right_half = mergesort(arr[mid:])

    return merge(left_half,right_half)

def merge(left_half, right_half):
    i=j=0
    sorted_arr = []

    while(i<len(left_half) and j<len(right_half)):
        if(left_half[i]<right_half[j]):
            sorted_arr.append(left_half[i])
            i+=1
        else:
            sorted_arr.append(right_half[j])
            j+=1
    sorted_arr.extend(left_half[i:])
    sorted_arr.extend(right_half[j:])

    return sorted_arr




n = int(input('Enter total numbers'))

arr = list(map(int,input(f"Enter {n} space numbers").split()[:n]))
print(mergesort(arr))

#Time complexity - O(n log n) for all cases