name = input("Enter your name ")
age = int(input("Enter your age"))

numbers = list(map(int, input("Enter the numbers").split()))

print("Using f-string")
print(f"Your name is {name} and your age is {age}")
        
print("Using format string")
print("Your name is {} and your age is {}".format(name,age))

print("Using concatenation")
print("Your name is "+name+" and your age is "+str(age))


print("You have entered the numbers",numbers)