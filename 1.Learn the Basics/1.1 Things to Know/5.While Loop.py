'''
While loop is generally used to execute a block of code repeatedly as long as a given condition is True.
It is typically used when we didn't know the beforehand how many iterations we need to perform, and we need to perform
until the condition is met.
'''

i = 0
while i < 5:
    print(i)
    i+=1 

#Infinite loop with break condition

count = 0 
while True:
    print("This will print 5 times")
    count+=1
    if(count==5):
        break

#While loop with Else: - While loop paired with else which runs if the loop completes normally without a break.
i=0
while i<5:
    print("Still Exists")
    i+=2
    if(i==2):
        break 
else:
    print("Else part is running")

'''
Infinite Loops: If the condition in a while loop is always True, the loop will run forever. 
This is called an infinite loop.
Make sure there is a way to stop the loop (e.g., using a break or an external condition).
'''

#break - Exits the loop entirely regardless of the condition 
#continue - Skips the rest of the code in the current iteration and move to the next iteration 

i = 0 

while i<10:
    
    i+=1
    if(i==4):
        continue
    print(i)
    if(i==7):
        break 

'''
Summary:

while loop: Repeats code as long as a condition is True.
Break: Exits the loop immediately.
Continue: Skips the rest of the code in the current iteration and moves to the next iteration.
else block: Executes after the loop finishes if there was no break.
'''