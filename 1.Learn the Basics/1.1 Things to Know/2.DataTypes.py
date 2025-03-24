# --- Numeric Types ---

# int - Integer Values (Postive/Negative/Zero)
x=50
y=-5 
print(type(x))

# float - Floating - point number(decimal values)
p = 3.14 
print(type(p))

#complex - Complex numbers (Where j is the imaginary part)
z=2+3j
print(type(z))

# --- Sequence Types --- 

#str - Sequence of characters 
name = "Python"
print(type(name))

#List - Mutable ordered collection of items 
numbers = [1,2,3,4,5]
numbers.append(5)
print(type(numbers))

#Tuple - Immutable ordered collection of items 
coordinates = (10,20,30)
print(type(coordinates))

# --- Mapping Type ---
#Dict
student = {"name":"praveen","age":27}
print(type(student))

# --- Set Types --- 
#set - Mutable set of unique items 
fruits = {"apple","apple","banana"}
print(type(fruits)) #It will skip the additional duplicate "apple"

#frozen-set Immutable set of unique items 
frozen_fruits = frozenset(["apple","apple","orange"])
print(type(frozen_fruits))

# --- Boolean --- 
isActive = True 
print(type(isActive))

# --- None Type --- 
value = None 
print(type(value))


'''
--- Type Conversion --- 
Convert to an integer: int()
Convert to a float: float()
Convert to a string: str()
Convert to a list: list()
Convert to a tuple: tuple()
Convert to a set: set()


Immutable: Cannot be changed after creation (e.g., int, float, str, tuple, frozenset).
Mutable: Can be changed after creation (e.g., list, dict, set).

Why Use Immutable Types?
Safety in Multi-threading: 
    Immutable objects can be shared between threads without the risk of data being modified.
Hashability: 
    Immutable objects (like int, str, tuple, frozenset) are hashable and can be used as keys in dictionaries or elements in sets.
'''

x=21 
print(id(x)) #Both will have different memory address
x=x+22
print(id(x)) #Both will have different memory address
x=21 
print(id(x))

'''
The term immutable means that once an object is created, its content or state cannot be changed. Any operation that seems to modify the object actually creates a new object rather than altering the original one.
'''

numbers = [1,2,3,4,5]
print(id(numbers)) # Both will have the same memory address
numbers.append(66)
print(id(numbers)) # Both will have the same memory address