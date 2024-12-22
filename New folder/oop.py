class Customer:

 def identify(self, name):  
    print("I am Customer " + name)

cust = Customer()  
cust.identify("Laura")
class Customer2:
 def	__init__(self, name, balance):  
     self.name = name
     self.balance = balance
print("The	init	method was called")
cust = Customer2("Lara de Silva", 1000)  
print(cust.name)
print(cust.balance)
class Customer:
    
    def __init__(self, name, balance=5):  
        self.name = name
        self.balance = balance
        print("The init method was called")
        
    def __str__(self):
        return 'Customer: ' + str(self.name) + ', balance: ' + str(self.balance)
    
    def __repr__(self):
        return f"Customer(name={self.name}, balance={self.balance})"
    
    # Equality check
    def __eq__(self, other):
        return self.balance == other.balance
    
    # Less than comparison
    def __lt__(self, other):
        return self.balance < other.balance
    
    # Less than or equal to comparison
    def __le__(self, other):
        return self.balance <= other.balance
    
    # Greater than comparison
    def __gt__(self, other):
        return self.balance > other.balance
    
    # Greater than or equal to comparison (already provided in the original)
    def __ge__(self, other):
        return self.balance >= other.balance
    
    # Addition of balances between two Customer objects
    def __add__(self, other):
        return Customer(self.name + ' & ' + other.name, self.balance + other.balance)
    
    # Subtraction of balances between two Customer objects
    def __sub__(self, other):
        return Customer(self.name + ' & ' + other.name, self.balance - other.balance)

# Creating Customer instances
customer1 = Customer("Alice", 10)
customer2 = Customer("Bob", 7)
customer3 = Customer("Charlie", 10)
class Employee:

        def __init__(self , b = 15):
            self.balance = b
            print('Employee created.')

        def __add__(self , other):
            return Employee(self.balance - other)

        def __del__(self):
            print('Destructor called, Employee deleted.')

obj1 = Employee()
obj2 = obj1 + 10
print(obj2.balance)
del obj2
class Employee:
    # Class variable
    company_name = "TechCorp"

    def __init__(self, name):
        self.name = name


e1 = Employee("Alice")
e2 = Employee("Bob")

print(e1.company_name)  
print(e2.company_name)  

print(Employee.company_name)

Employee.company_name = "NewTechCorp"
print(e1.company_name) 
print(e2.company_name) 


e1.company_name = "Test"
print(e1.company_name)  
print(e2.company_name)  
print(Employee.company_name)  
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


r = Rectangle(10, 5)
print(f"Area: {r.area()}")  
print(f"Perimeter: {r.perimeter()}")  