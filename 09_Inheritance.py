print('--------------------single-------------------------------')
class company():                          # Parent class / Base class
    def company_info(self):               # Method of parent class
        print('Company : TCS')

class employee(company):                  # Child class; inherits from company
    def emp_info(self):                   # Method of child class
        print('Emp Name : Rahul')

emp1 = employee()                         # Create object of child class
emp1.emp_info()                           # Calls employee's own method
emp1.company_info()                       # Calls inherited method from company

print('--------------------single with constructor-------------------------------')
class company():                              # Parent class / Base class
    def __init__(self, com_name):              # Parent class constructor
        self.com_name = com_name               # Store company name in object

    def company_info(self):                    # Parent class method
        print(f'Company : {self.com_name}')


class employee(company):                       # Child class inherits from company
    def __init__(self, emp_name, com_name):    # Child class constructor
        self.emp_name = emp_name               # Store employee name
            # We can handle the company name in two ways:
            # 1. Store it directly in the child class
        #self.com_name = com_name               # Store company name
            # 2. Call the parent class constructor  
        company.__init__(self,com_name) # Call parent constructor

    def emp_info(self):                        # Child class method
        print(f'Emp Name : {self.emp_name}')

    def com_info(self):                        # Child class method
        company.company_info(self)             # Explicitly call parent method
        super().company_info()                 # Call parent method using super()
                                # super() refers to the next class in the inheritance hierarchy (one level up)      


emp1 = employee('Vicky', 'TechM')              # Create employee object
                                               # employee.__init__() is called
emp1.emp_info()                                # Calls employee's own method
emp1.company_info()                            # Calls inherited parent method
emp1.com_info()                                # Calls com_info(), which calls parent method


print('--------------------Multiple with constructor-------------------------------')
class company():                              # Parent class 1
    def __init__(self, com_name):             
        self.com_name = com_name              

    def company_info(self):                   
        print(f'Company : {self.com_name}')

class state():                                # Parent class 2  
    def __init__(self,state_name):
        self.state_name = state_name

    def state_info(self):
        print(f'state : {self.state_name}')    

class employee(company,state):                       # Child class inherits from company
    def __init__(self, emp_name, com_name, state_name):    # Child class constructor
        self.emp_name = emp_name               # Store employee name
          
        company.__init__(self,com_name) # Call parent 1 constructor
        state.__init__(self,state_name) # Call parent 2 constructor

    def all_info(self):                        # Child class method
        print(f' Emp Name : {self.emp_name} \n Company name : {self.com_name} \n state : {self.state_name}' )

    def call_parentMethod(self):                        # Child class method
        company.company_info(self)             # Explicitly call parent method
        state.state_info(self)
       
                        
emp1 = employee('Vicky', 'TechM', 'RJ')              # Create employee object
                                               # employee.__init__() is called
emp1.all_info()                                # Calls employee's own method
emp1.company_info()
emp1.state_info()

print('--------------------Multilevel with constructor-------------------------------')
class company():                              # Level 1: Base/Grandparent class
    def __init__(self, com_name):              
        self.com_name = com_name               

    def company_info(self):                    
        print(f'Company : {self.com_name}')    

class state(company):                          # Level 2: state inherits from company
    def __init__(self, state_name, com_name):  
        self.state_name = state_name           

        company.__init__(self, com_name)       # Explicitly call company constructor to initialize com_name

    def state_info(self):                      
        print(f'state : {self.state_name}')    

class employee(state):                         # Level 3: employee inherits from state
    def __init__(self, emp_name, com_name, state_name):  
        self.emp_name = emp_name               

        state.__init__(self, state_name, com_name)       # Explicitly call state
                                                         # constructor
                                                         # state constructor then
                                                         # calls company constructor

    def all_info(self):                        # Employee's own method
        print(f' Emp Name : {self.emp_name} \n Company name : {self.com_name} \n state : {self.state_name}')

    def call_parentMethod(self):               # Method to explicitly call parent methods
        company.company_info(self)             # Explicitly call company class method
        state.state_info(self)                  # Explicitly call state class method

emp1 = employee('Vicky', 'TechM', 'RJ')
emp1.all_info()                                # Call employee's own method
# emp1.company_info()                            # Call inherited method from company
# emp1.state_info()                              # Call inherited method from state
# emp1.call_parentMethod()                     # Calls both parent class methods explicitly