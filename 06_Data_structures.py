print('----------------------------------List------------------------------------------')
# A list stores multiple values in [ ], and it allows duplicate values.
# List elements are ordered and can be accessed using their index.

mylist = ['vikcy',33,'hyd',['mamata',28],'aa','bb','cc']

print(mylist[:])
print(mylist[0]) # To get the first value from a list, use index 0.
print(mylist[3])
print(mylist[3][0]) # To get a value from a nested list, use multiple indexes.
print(mylist[0:3]) # To get values from a list within a range of positions, use slicing.
print(mylist[-2:]) # To get values from the end of a list, use negative indexing.
print(mylist[len(mylist)-2:len(mylist)]) # for the above, system will perform this internally
print(mylist[::2]) # # step value can be any number to jump between positions
print(mylist.index('hyd'))# find position of a value


print('----------------------------------List - Operations------------------------------------------')
mylist.append('jaisalmer') # add value at the end
print(mylist[:])

mylist.insert(1,'male') # add value at a specific position
print(mylist[:])

mylist.pop() # remove value using position by default last position
print(mylist[:])   

mylist.remove(33) # remove a value
print(mylist[:])   

list_test = [30, 40, 30, 40, 10, 3]

list_test.reverse() # reverse permanent
print(list_test[:])

for i in reversed(list_test): # Reverses only at runtime; gives the result in different lines without changing the original list.
    print(i)

print(list_test[::-1]) # Reverses only at runtime;

list_test.sort()
print(list_test[:]) # sort() does not support different data types  

new_list = [i for i in list_test] # Creating a new list from an existing list
print(new_list[:])

new_list = [i*i for i in list_test] # Creating a new list from an existing list with an operation
print(new_list[:])

new_list = [i*i for i in list_test if (i % 2) == 0 ] # Creating a new list from an existing list with an operation and if condition
print(new_list[:])

list_test.clear()
print(list_test[:]) # remove all values 


print('-----------------------Dictionary----------------------------------')
# A dictionary stores data in { } as key-value pairs.
# Each value is accessed using its key instead of an index.

dictionary = {'name':'vicky','age':32} 
print(dictionary) 

dictionary['name'] = 'virendra' # Update the value of the "name" key
print(dictionary)

dictionary['surname'] = 'suthar' # Updates the value if the key exists; otherwise, creates a new key-value pair
print(dictionary)

dictionary.pop('surname') # delete value
print(dictionary)

print(dictionary.keys()) # print all keys
print(dictionary.values()) # print all values
print(dictionary.items()) # print pairs


dictionary = {'name':'vicky','age':32, 'wife':{'name' : 'mamatha', 'age' : '27'}} # Dictionary inside another dictionary
print(dictionary) 
print(dictionary['wife']) # to get inside dictionary
print(dictionary['wife']['name']) # to get inside dictionary specific key value


print('-------------------------------set--------------------------')
# A set also stores values using { }, similar to a dictionary, but without key-value pairs.
# Sets are mainly useful for mathematical operations like union, intersection, and difference.

my_set = {1,2,3,4,5,5,4,5}
print(type(my_set))
print(my_set) # set automatically removes duplicate values.

new_set = {1,2,6,7,7}

print(new_set.union(my_set)) # union both set
print(new_set.intersection(my_set)) # intersection - only common values

my_set.remove(2) # remove value from set
print(my_set)

my_set.add(15) # add value into set
print(my_set)

a={} # Creates an empty dictionary
b=set() # Creates an empty set

print(type(a),type(b))


print('-------------------------------tuple--------------------------')
# A tuple stores multiple values in ( ), and its elements cannot be changed after creation.
# Tuple elements are ordered and can be accessed using their index.
# We can convert a tuple into a list, perform list operations, and convert it back to a tuple.


my_tuple = (1,2,3,3) # A tuple does not remove duplicate values; duplicate values are allowed

print(my_tuple)

my_tuplist = list(my_tuple) # convert into list

my_tuplist.append(10) # append new value

print(my_tuplist)

my_tuple = tuple(my_tuplist) # convert into tuple

print(my_tuple)