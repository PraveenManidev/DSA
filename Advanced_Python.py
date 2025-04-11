'''Decorator:
-- Decorator is an higher order function that modifies or extends the behaviour of the another 
function without modifying the actual code.
-- This takes a function as a input and adds some functionality and returns the
 modified function
'''

def my_decorator(func):
    def wrapper():
        print('Before calling the function')
        func()
        print('After calling the function')
    return wrapper 

@my_decorator
def say_hello():
    print('This is called in decorator function')

say_hello()

###################################################################
'''
Generator:
-- This is a special type of iterable that yields values one at a time, instead of storing them in memory 
all at once. This makes them efficient for handling large data sets.

-- A normal function returns a values and terminates but generator yields values one by one and can be resumed 
from where it left off
'''

def get_numbers():
    for i in range(1,6):
        yield i 

gen = get_numbers()

print(next(gen))

print(next(gen))

print(next(gen))
