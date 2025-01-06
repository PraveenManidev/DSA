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