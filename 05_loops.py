print('-------------------for loop--------------------------------')

my_list = ['product','customer','price']

for i in my_list:
    print(i)

print('-------------------for loop with if--------------------------------')

for i in my_list:
    if(i.lower()=='product'):
        print('product table')
    else:
        print('not product table')

print('-------------------for loop with if and nested loop--------------------------------')

for i in my_list:
    if(i.lower()=='product'):
        for x in i:
            print(x)

print('-------------------for loop with if and break--------------------------------')

for i in my_list:
    if(i.lower()=='product'):
        print('product table')
        break
    else:
        print('not product table')       

print('-------------------for loop with if and continue--------------------------------')

for i in my_list:
    if(i.lower()=='customer'):
        continue
        print('product table')        
    else:
        print(i)                 
    
print('-------------------for loop - range--------------------------------')

for i in range(1,6): # range(start, end) generates numbers from start to end - 1.
    print(i)

print('-------------------while loop--------------------------------')
x=1

while(x<3):
    print(x)
    x=x+1

print('-------------------while loop with break--------------------------------')
x=1

while(1==1):
    print(x)
    x=x+1
    if(x>3):
        break

