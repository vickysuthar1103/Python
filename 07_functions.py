
from sys import exception
print('----------------------function without param----------------------------------')
x =10

def my_func():
    if(x>10):
        print('more then 10')
    else:
        print('less then 10')

my_func()

x=11
my_func()

print('----------------------function with param----------------------------------')

def my_func(y):
    if(y>10):
        print('more then 10')
    else:
        print('less then 10')

my_func(20)

testvar=5
my_func(testvar)

print('----------------------function with param and return----------------------------------')

def my_func(y):
    if(y>10):
        print('more then 10')
    else:
        print('less then 10')

    return y

testvar=5
return_var = my_func(testvar)
print(return_var)

print('----------------------function with multi param and return----------------------------------')

def my_func(x,y):
    #return 'x = ' + str(x) + ', y = ' + str(y) + ', result = ' + str(x * y) # Convert int values to str because we are combining numbers with strings.
    return f'x = {x}, y = {y}, result = {x * y}' # f-string allows us to directly insert variable values into a string.
    # we can use any return statement

x = 10
y = 5
return_var = my_func(x,y)
print(return_var)

print('----------------------function with default value----------------------------------')

def my_func(x,y = 15):
    print(x*y)

x = 10
y = 5
my_func(x,y) # If we pass a value, the function uses the passed value; otherwise, it uses the default value.
my_func(x)


print('----------------------function with tuple----------------------------------')
# When we don't know how many values will be passed, we use *variablename.
# It can accept multiple values, which are stored as a tuple.

def my_func(*x): 
    print(type(x),x)

my_func(10,20,30,40,50)

print('----------------------function with dictionary----------------------------------')
# When we use **, the values are stored in a dictionary.
# It can accept multiple key-value pairs, which are stored as a dictionary.

def my_func(**x): 
    print(type(x),x)

my_func(x = 10, y = 20, z=30)

print('----------------------lamda function----------------------------------')
#A lambda function is a small, anonymous function used for a simple operation. It is written in one line.

lamdafunction = lambda x,y : x+y

result = lamdafunction(10,20)
print(result)

print('----------------------function - map----------------------------------')
# map() applies a function to each value in an iterable.

def square(x):
    return x*x

my_list=[10,20,30]

# map() applies the function to each value in the list
# map() returns a map object, so we convert it into a list
result = list(map(square,my_list))
print(result)

print('----------------------function - filter----------------------------------')
# map() is used to perform an operation on every value.
# filter() is used to select values based on a condition.

def square(x):
    if(x % 2 == 0):
        return x*x

my_list=[10,20,25]

# map() applies the function to every value in the list
result = list(map(square,my_list))
print(result)

# filter() keeps only the values for which the function returns True
result = list(filter(square,my_list))
print(result)


print('----------------------function - reduce----------------------------------')
# reduce() takes two values at a time, uses the result with the next value,
# and continues until all values are processed.

from functools import reduce # reduce() is not a built-in function, so we need to import it


def square(x,y):
        return x*y

my_list=[5,2,3]

# reduce() applies the function repeatedly and returns a single value 
# First: 5 * 2 = 10
# Then: 10 * 3 = 30

result = reduce(square,my_list)
print(result)

# map()    → applies function to every value
# filter() → selects values based on a condition
# reduce() → combines values into a single value


print('----------------------Exception handling----------------------------------')
x = '10'

try:
    # x is a string, but 10 is an integer.
    # Python cannot compare string and integer using >, so it will raise a TypeError.
    if x > 10:
        print('x more then 10')
    else:
        print('x less then or equal to 10')

# except:
#    # If any error occurs inside the try block, except will handle the error.
#    print('errorrrrr')

except Exception as e:
    # Exception as e stores the error information in variable 'e'.
    print(e)

finally: 
    # Finally block will always run, whether an error occurs or not.
    # Finally block is optional, not mandatory.
    print('finally block - always run')    

# This line will execute even if an error occurs in the try block.
print('hello.....')

print('----------------------f-string----------------------------------')
name = 'vicky'

statement= f'my name is {name}'

print(statement)
print(f'name = {name}')

print('----------------------global variable----------------------------------')
x = 10  # Global variable

def test():
    x = 5  # Local variable; it takes priority over the global variable inside this function.
    print(x)  # Prints the local variable x because it is defined inside the function.

test()

print('----------------------enumerate----------------------------------')
my_list = [10, 20, 30]

print('output 1')

for i in my_list:
    # Directly get each value from the list.
    print(i)


print('output 2')

for i in enumerate(my_list):
    # enumerate() returns both the position (index) and the value.
    # The result is returned as a tuple: (position, value).
    print(i)


print('output 3')

for i, x in enumerate(my_list):
    # i stores the position (index).
    # x stores the value at that position.
    print('position = ', i)
    print('Value = ', x)

print('----------------------custom Exception----------------------------------')
x = 10

if x == 10:
    # raise is used to manually generate an exception.
    # Exception is the built-in exception class.
    raise Exception('x is equal to 10')

