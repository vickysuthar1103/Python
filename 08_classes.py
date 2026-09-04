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