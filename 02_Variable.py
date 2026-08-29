# single line comment
''' Multi-line 
comment.'''


from typing import cast
First_name = 'vicky'
Last_name = "suthar"
age = 34
yearone = 1

print(First_name) # string
print(First_name + ' ' +Last_name) # Concatenate the strings.
print(First_name,age) # string and number
print('next age ', age+yearone) # string and number using an operation

print('-----------------------------1-----------------------------------')

x,y,z = 10,11,12 # Multiple variable assignment in a single line.
print(x,y,z)

x=y=z = 10 # Assign the same value to multiple variables.
print(x,y,z,sep='|')

print('-----------------------------2-----------------------------------')

x = 20+\
    10 # Backslash (\) allows code to be written across multiple lines.
print(x)    

x = (20+
    10) # Parentheses () also allow code to be written across multiple lines.
print(x) 

print('-----------------------------3-----------------------------------')

print('Explicit type casting')
x='10'
y=10
print(type(x),type(y)) # show class type

x_new = int(x) #Explicit type casting
y_new = str(y) #Explicit type casting
print(type(x_new),type(y_new))


print('\nimplicit type casting')

x = 10
y = 10.5
print(type(x),type(y)) 

z=x+y #implicit type casting
print(type(z))
