'''
#Number of occurances
def number_of_occurences(array,query):

    hash_arr = [0]*13

    for num in array:
        hash_arr[num]+=1
    for que in query:
        print(hash_arr[que])

n = int(input())
array = list(map(int,input().split()[:n]))

q = int(input())
query = [int(input()) for i in range(q)]

number_of_occurences(array,query)


#Character_of_Occurances
def ch_occurences(str,query):
    hash_arr = [0]*13

    for s in str:
        index = ord(s)-ord('a')
        hash_arr[index]+=1
    for q in query:
        index = ord(q)-ord('a')
        print(hash_arr[index])
s = input().strip()
q = int(input())
query = [(input().strip().lower()) for i in range(q)]
ch_occurences(s,query)

'''
#Find the max and min occurances 
def max_min_occurences(arr):
    freq_arr = {}

    for num in arr:
        freq_arr[num] = freq_arr.get(num,0)+1

    print("Frequency Array",freq_arr)

    max_freq = max(freq_arr.values())
    min_freq = min(freq_arr.values())

    most_frequent = [key for key, val in freq_arr.items() if val == max_freq]
    least_frequent = [key for key, val in freq_arr.items()if val == min_freq]

    print('Most',most_frequent)
    print('Least',least_frequent)

arr = [10,5,10,5,15,5]

max_min_occurences(arr)