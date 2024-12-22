# Single Responsibility Principle - SRP
class Invoice:
    def __init__(self, amount):
        self.amount = amount

    def calculate_tax(self):
        return self.amount * 0.1  # حساب الضريبة

class InvoicePrinter:
    def print_invoice(self, invoice):
        print(f"Invoice Amount: {invoice.amount}")
        print(f"Tax: {invoice.calculate_tax()}")
class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

class OrderProcessor:
    def process_order(self, order):
        print(f"Processing order {order.order_id} with amount {order.amount}")

class OrderRepository:
    def save_order(self, order):
        print(f"Saving order {order.order_id} to the database")
        
# Open/Closed Principle - OCP
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this!")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def calculate_area(shapes):
    return sum(shape.area() for shape in shapes)

shapes = [Circle(5), Rectangle(2, 3)]
print(calculate_area(shapes))  
    
# Liskov Substitution Principle - LSP
class Bird:
    def fly(self):
        print("Flying")

class Sparrow(Bird):
    pass

class Ostrich(Bird):
    def fly(self):
        raise Exception("I can't fly")  
# Interface Segregation Principle - ISP    # 
class Worker:
    def work(self):
        pass

    def eat(self):
        pass

class Robot(Worker):
    def work(self):
        print("Working...")

    def eat(self):
        pass  

class Human(Worker):
    def work(self):
        print("Working...")

    def eat(self):
        print("Eating...")

class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Robot(Workable):
    def work(self):
        print("Working...")

class Human(Workable, Eatable):
    def work(self):
        print("Working...")

    def eat(self):
        print("Eating...")
class Printer:
    def print(self):
        pass

class Scanner:
    def scan(self):
        pass

class AllInOnePrinter(Printer, Scanner):
    def print(self):
        print("Printing...")

    def scan(self):
        print("Scanning...")

class SimplePrinter(Printer):
    def print(self):
        print("Printing...")
        
# Dependency Inversion Principle - DIP
class LightBulb:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")

class Switch:
    def __init__(self, bulb):
        self.bulb = bulb

    def operate(self):
        self.bulb.turn_on()

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")

class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self):
        self.device.turn_on()
class DatabaseConnection:
    def connect(self):
        print("Connecting to the database")

class Application:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def start(self):
        self.db_connection.connect()
        print("Application started")

# استخدام الواجهة لتحقيق التبعيات
class IConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

class DatabaseConnection(IConnection):
    def connect(self):
        print("Connecting to the database")

class Application:
    def __init__(self, db_connection: IConnection):
        self.db_connection = db_connection

    def start(self):
        self.db_connection.connect()
        print("Application started")

db_connection = DatabaseConnection()
app = Application(db_connection)
app.start()
        


