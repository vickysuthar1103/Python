class employee():
    emp_name = 'vicky' # inside class variable call as attribute
    emp_dept = 'IT' 
    
    def result(self): # function inside class is called method
        print(f'Employee name = {self.emp_name}, dept = {self.emp_dept}') # self is used to access class attributes

    def resultwithparam(self,emp_name,emp_dept): # method with parameters
        print(f'Employee name = {emp_name}, dept = {emp_dept}') # emp_name and emp_dept are parameters passed to the method
    

emp1 = employee() # creating an object of employee class

print(emp1.emp_name) # accessing class attribute using object

emp1.result() # calling method using object

emp1.resultwithparam(emp_name='rahul',emp_dept='sales') # passing values using keyword arguments

emp1.resultwithparam('rahul','sales') # passing values using positional arguments

print('---------------------Constructor----------------------------------------')

class employee():
    companyname = 'xyz'

    def __init__(self): # Constructor; automatically called when an object is created
        # 'pass' Use pass if you don't want to execute anything in the constructor
        #pass 
        print('Hello')

    def resultwithparam(self,emp_name,emp_dept): # method with parameters
        print(f'Employee name = {emp_name}, dept = {emp_dept}') # emp_name and emp_dept are parameters passed to the method
    
emp=employee() # __init__() is automatically called here, so it prints "Hello"

print('---------------------Constructor with param----------------------------------------')

class employee():
    companyname = 'xyz'

    def __init__(self,emp_name,emp_dept): # Constructor; automatically called when an object is created
        self.emp_name = emp_name # Create an instance variable for employee name
        self.emp_dept = emp_dept # Create an instance variable for employee dept
        
    def info(self):
        print(f'Employee name = {self.emp_name}, dept = {self.emp_dept}, company name = {self.companyname}')

    @staticmethod
    # @staticmethod tells Python that this method does NOT need self or cls
        # It does not depend on any object-specific data or class-level data
        # Therefore, we can call this method without creating an object
        # We use @staticmethod when a function logically belongs to the class
        # but does not need to access object or class variables
    def add(x,y): # Static method; no self is required
        print(x+y)        
    
emp=employee('mamatha','IT') # __init__() is automatically called here
emp.info()

emp2=employee('vicky','HR')
emp2.companyname = 'TCS'
emp2.info()

emp.info() # emp still uses the class variable companyname = 'xyz'

employee.companyname = 'TechM'
emp.info()
emp2.info()

emp.add(10,20)
employee.add(1,5)

print('--------------------- class method ------------------------------')

class employee():

    companyname = 'xyz'  # Class variable; shared by all objects

    def __init__(self, companyname):
        self.companyname = 'abc'  # Instance variable; belongs to the object


    @classmethod
    def changeinclassmethod(cls, companyname):
        # cls refers to the class (employee)
        # This changes the class variable
        cls.companyname = companyname


# Initially, class variable contains 'xyz'
print('Class variable before change =', employee.companyname)

# Create an object
emp = employee('TCS')

# emp.companyname refers to the instance variable
print('Instance variable =', emp.companyname)

# employee.companyname refers to the class variable
print('Class variable =', employee.companyname)

# Call class method and change class variable from 'xyz' to 'TCS'
employee.changeinclassmethod('TCS')

# Instance variable is still 'abc'
print('Instance variable after class method =', emp.companyname)

# Class variable is now 'TCS'
print('Class variable after class method =', employee.companyname)

print('--------------------- getter and setter ------------------------------')
# getter and setter are commonly used with @property 
# to control how we read and update an instance variable.

class employee():

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # _salary is treated as an internal/private variable


    @property
    def salary(self):
        # Getter
        # Used when we want to READ the salary
        return self._salary


    @salary.setter
    def salary(self, salary):
        # Setter
        # Used when we want to CHANGE the salary
        # We can also add validation before changing it
        if salary > 0:
            self._salary = salary
        else:
            print('Salary must be greater than 0')


# Create object
emp = employee('Vicky', 50000)

# Getter is automatically called
# We don't need to write emp.salary()
print('Current salary =', emp.salary)


# Setter is automatically called
# We don't need to write emp.salary(60000)
emp.salary = 60000

# Getter is called again
print('Updated salary =', emp.salary)

# Setter validation
emp.salary = -1000