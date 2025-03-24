'''
In Python, the concept of passing by reference or passing by value is a little different from languages like C++ or Java. 
This difference is because Python uses a model called "pass by object reference" or "pass by assignment".

If the object is mutable (list,dict or sets) then the changes made to the objects inside the functions 
will affect original object outside the function.

If the object is mutable (integer, float, strings, tuples) then the changes made to the objects inside the functions 
will not affect original object outside the function.
'''

# Pass by Reference for mutable objects:
def modify_list(lst):
    lst.append(5)
    print("Inside the function", lst)


list = [1,2,3,4]
print(list)
modify_list(list)
print("Outside the list",list)

# Pass by value for immutable objects: - New object will be created and the original object remains unchanged.

def modified_x(x):
    print("Inside",x,id(x))
    x=x+1
    print("Inside",x,id(x))

x = 10 
print(x,id(x))

new_X = modified_x(x)
print(x,id(x))

'''
Effects of Assignment for Mutable vs Immutable Types

Mutable types (like lists and dictionaries) can be modified directly inside the function, 
so the changes reflect in the original object.
Immutable types (like integers, strings, and tuples) create new objects when reassigned inside the function,
 and the original object remains unaffected.
'''

'''
Summary:
Python passes all function arguments by object reference.
Mutable objects can be modified, so they act like "pass by reference."
Immutable objects cannot be modified, so they act like "pass by value" because any modification creates a new object.
'''