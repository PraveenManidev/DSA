# Lists are mutable which is their elements can be changed after the creation.

fruits = ["apple","orange","mango"]
fruits.append("cherry")
fruits.insert(4,"banana")
fruits.remove("apple")
fruits.pop(3)
fruits.sort()

print(fruits)


'''
List Methods
-- append(item) : Adds an item at the end.
-- insert(index, item): Adds an item at a specific index.
-- remove(item): Removes the first occurrence of an item.
-- pop(index): Removes and returns the item at the specified index.
-- sort(): Sorts the list in ascending order.
'''

### --- Strings --- 
greetings = "Hello, World!"
print(greetings)

#Accessing the character in the String 
print(greetings[9])

#Slicing Strings 
subString = greetings[0:5] #Extracts the string from 0 to 4 and exclude 5
print(subString)



"""
Common String Methods
lower(): Converts to lowercase.
upper(): Converts to uppercase.
strip(): Removes leading and trailing whitespace.
split(): Splits the string into a list of substrings.
join(): Joins a list of strings into one string.
"""
