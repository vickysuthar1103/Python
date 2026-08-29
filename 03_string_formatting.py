name = 'virendra' # Python stores a string as a sequence of characters, and each character can be accessed using an index.

print(name[0],name[5]) #To print a character at a specific position in a string
print(name[0:4]) #To print characters from multiple continuous positions in a string, called as slicing

#In Python slicing, the start index is included, but the end index is excluded (n-1). \
# For example, in "virendra", positions are 0,1,2,3,4,5,6,7. If the end point is 6, \
# characters from position 0 to 5 (6-1) will be printed.

print(name[3:6])

print(name[0:]) # If the end position is not provided, Python considers the string's length as the end position.
print(name[:6]) # If the start position is not provided, Python considers it as 0.
print(name[:]) # If both start and end positions are not provided, the start position is considered 0 and the end position is considered the length of the string.

print('-----------------------------------string fucntion--------------------------------------')
print(len(name))
print(name.lower()) # convert into upper case
print(name.upper()) # convert into lower case
print(name.capitalize()) # convert the first character of a string to uppercase
print(name.replace('v','d')) # replace() function is used to replace a character or substring with another character or substring in a string.
print(name.replace('vir','d'))

#----------------------------
full_name = 'virendra suthar'
my_list = full_name.split(' ')
print(my_list)

#----------------------------
file = 'customer.csv'
if(file.endswith('.csv')):
    print('CSV file')

if(file.startswith('cust')):
    print('customer file')    

#----------------------------------
statement = 'Hello hello hello guys'
print(statement.count('hello'))  # One "Hello" is in uppercase, so it will be ignored.

#---------------------------------
x = 'name'
y = '10'
z = '10name'
print(x.isnumeric()) # To check whether a string contains only numeric characters.
print(y.isnumeric()) # isnumeric() and similar functions only work with strings.
print(z.isnumeric())
