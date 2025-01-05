# For loops iterates over the each and every item over the sequences (list, tuple, dictionary, strings)

fruits = ["apple","banana","cherry"]

for item in fruits:
    print(item)

#Iterating in String:
word = "Hello"

for letter in word:
    print(letter)

#Iterating in Range:
for i in range(2,10,2): #Starts at 2 and ends at 9 and steps by 2
    print(i)

#Iterating over dictionary:
person = {"name":"praveen","age":27,"location":"Cheyur"}
for key in person:
    print(key,":",person[key])

for key, value in person.items(): #Using items
    print(key,":",value)

#Nested for loops:

for i in range(3):
    for j in range(5):
        print(f"i:{i},j:{j}")

#Using else with For Loop: - Python allows else to follow a for loop if the loop continues without hitting the break stmt

for i in range(5):
    print(i)
else:
    print("Loop completed successfully")

for i in range(5):
    if(i==3):
        break
    print(i)
else:
    print("Loop completed successfully")
