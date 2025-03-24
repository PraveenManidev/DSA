################## PATTERN PROBLEM ############
'''
* * * *
* * * *
* * * *
* * * *
'''

for i in range(4):
    for j in range(4):
        print("* ",end="")
    print()

##############################################

'''
*
* *
* * *
* * * *
'''

for i in range(0,4,1):
    for j in range(0,i+1,1):
        print("* ", end="")
    print()

##############################################

'''
1
1 2
1 2 3
1 2 3 4
'''

for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(j, end="")
    print()

##############################################

'''
1
2 2
3 3 3
4 4 4 4
'''

for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(i, end="")
    print()

##############################################

'''
* * * * *
* * * * 
* * *
* * 
*
'''
n=6
for i in range(1,n,1):
    for j in range(1,n-i+1,1):
        print("* ",end="")
    print()

##############################################
'''
1 2 3 4 5
1 2 3 4 
1 2 3 
1 2 
1
'''

n=6
for i in range(1,n,1):
    for j in range(1,n-i+1,1):
        print(j, end="")
    print()

#############################################

'''
    *
  * * * 
* * * * *
'''
n=5
for i in range(0,n,1):
    for j in range(0, n-i,1):
        print("  ",end="")
    for j in range(0, 2*i+1,1):
        print("* ",end="")
    for j in range(0, n-i,1):
        print("  ",end="")
    print()

####################################################

'''
* * * * *
  * * *
    *
'''

n=5
for i in range(0,n,1):
    for j in range(0,i+1,1):
        print("  ",end="")
    for j in range(0,2*n-(2*i+1),1):
        print("* ",end="")
    for j in range(0,i+1,1):
        print("  ",end="")
    print()


#################################################################

'''
*
**
***
****
*****
****
***
**
*
'''

n = 6
for i in range(1,2*n-1,1):
    stars = i
    if i>n:
        stars = 2*n-i
    for j in range(1,stars,1):
        print("*", end="")
    print()

################################################################
'''
1
01
101
0101
10101
'''

n=6
for i in range(0,n,1):
    num = 0 if (i%2==0) else 1
    for j in range(0,i,1):
        print(num,end="")
        num = 1-num 
    print()

################################################################
'''
1         1
12       21
123     321
1234   4321
12345 54321
'''
n = 6
space = 2 * n - 3  # Initial number of spaces

for i in range(1, n):
    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end="")
    
    # Print spaces
    for j in range(1, space + 1):
        print(" ", end="")
    
    # Print decreasing numbers
    for j in range(i, 0, -1):
        print(j, end="")
    
    # Move to the next line
    print()
    
    # Decrease the number of spaces for the next row
    space -= 2

########################################################
'''
A
AB
ABC
ABCD
ABCDE
ABCDEF
'''
n = 6
for i in range(0,n,1):
    for j in range(0,i+1,1):
        print(chr(65+j),end="")
    print()

#######################################################
'''
     A
    ABA
   ABCBA
  ABCDCBA
 ABCDEDCBA
ABCDEFEDCBA
'''

n = 6  # Number of rows
for i in range(1, n + 1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end="")
    
    # Print increasing letters
    for j in range(0, i):
        print(chr(65 + j), end="")
    
    # Print decreasing letters
    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end="")
    
    # Move to the next line
    print()

#####################################################
'''
E
DE
CDE
BCDE
ABCDE
'''
last_char = 'E'
n = ord(last_char) - ord('A')+1
for i in range(n):
    start_char = ord(last_char)-i 
    for j in range(i+1):
        print(chr(start_char+j),end="")
    print()

#####################################################

'''
******
*    *
*    *
*    *
*    *
******
'''
n = 6
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
#####################################################
