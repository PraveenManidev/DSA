from datetime import datetime
from math import sqrt
current_time = datetime.now().strftime("%H:%M:%S")
print(current_time)

#Count Digits
n = 35012312
counter = 0
while(n>0):
    counter+=1
    n=n//10
print("Output-1",counter)

#Reverse a number skip zero's
n=12340000
revNum = 0
while(n>0):
    lastDigit = n%10
    revNum = (revNum*10)+lastDigit
    n=n//10
print("Output-2",revNum)

#Palindrome Number
n=123454321
revNum = 0
dup = n
while(n>0):
    lastDigit = n%10
    revNum = (revNum * 10)+lastDigit
    n=n//10
result = 'Palindrome' if (revNum==dup) else 'Not Palindrome'
print(result)

#Armstrong Number
n = 371
dup = n
sum = 0
while(n>0):
    lastDigit = n%10
    sum += lastDigit**3
    n=n//10
result = 'Armstrong Number' if (dup==sum) else 'Not Armstrong Number'
print(result)

#Print all divisors
n=36
for i in range(1,n+1):
    if(n%i==0):
        print(i,end=' ')
print()

### Alter method for divisors
n=36
for i in range(1,int((n**0.5)+1)):    
    if(n%i==0):
        print(i,end=' ')
        if(n//i!=i):
            print(n//i,end=' ')
print()
### Prime Number = A number which has two factors 1 and itself 
n=310
counter = 0
for i in range(1,int(n**0.5)+1):
    if(n%i==0):
        counter += 1
        if(n//i!=i):
            counter+=1
    if counter > 2:
        break
result = 'Prime' if(counter==2) else 'Not Prime'
print(result)

#GCD && HCF:
a=22
b=15
while(a>0 and b>0):
    if(a>b):
        a=a%b
    else:
        b=b%a 
result = b  if (a==0) else a
print(result)