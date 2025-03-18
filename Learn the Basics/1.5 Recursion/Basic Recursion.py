#Print linear number 
counter = 0
def fun():
    global counter
    if(counter>5):
        return
    print(counter)
    counter+=1
    fun()
fun()
print()

#Print in reverse order 
def fun(i,n):
    if(i<1):
        return
    print(i)
    fun(i-1,n)

n=3
fun(n,n)

#Sum of N numbers (Parameterized)

def add(i,sum):
    if(i<1):
        print("Sum",sum)
        return
    add(i-1,sum+i)
n=5
add(n,0)
print()

#Sum of N numbers (Functional)
def fun(n):
    if n==0:
        return 0
    return n+fun(n-1)
n=3
print(fun(n))

#Factorial of N numbers
def fact(n):
    if(n==0):
        return 1 
    return n*fact(n-1)

n=4
print(fact(n))

#Reverse an array
def rev(arr,i,n):
    if(i>n//2):
        return
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    rev(arr,i+1,n)
arr = [1,3,5,7,9]

rev(arr,0,len(arr))

print(arr)

#Palindrome
def palindrome(s,i,n):
    if(i>n//2):
        return 'Palindrome'
    if(s[i]!=s[n-i-1]):
        return 'Not Palindrome'
    return palindrome(s,i+1,n)
s = 'madama'
print(palindrome(s,0,len(s)))

#Fibonacci
def fibonacci(n):
    if(n<=1):
        return n
    return fibonacci(n-1)+fibonacci(n-2)
n=4
print(fibonacci(n))