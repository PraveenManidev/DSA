
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


#Find the max and min occurances 
def max_min_occurences(arr):
    freq_map = {}

    for num in arr:
        freq_map[num] = freq_map.get(num,0) + 1
    print(freq_map)
    
    max_element = max(freq_map.values())
    min_element = min(freq_map.values())

    most_frequency = [key for key, val in freq_map.items() if val== max_element]
    least_frequency = [key for key, val in freq_map.items() if val== min_element]

   
    print("most",most_frequency)
    print("least",least_frequency)



arr = [1,2,1,2,5,115,115]
max_min_occurences(arr)