# HERE I WILL APPLY THE SOLID PRINCIPLES
# Single Responsibility Principle (SRP)
# Open/Closed Principle (OCP)
# Liskov Substitution Principle (LSP)
# Interface Segregation Principle (ISP)
# Dependency Inversion Principle (DIP)
from abc import ABC, abstractmethod
class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total    
        
class Payment(ABC):
    @abstractmethod
    def pay(self, order, security_code):
        pass

class DebitPay(Payment):
    def pay(self, order, security_code):
        print("Processing debit payment...")
        print(f"Security code: {security_code}")
        order.status = "paid"
class CreditPay(Payment):
    def pay(self, order, security_code):
        print("Processing credit payment...")
        print(f"Security code: {security_code}")
        order.status = "paid"
class Paypal(Payment):
    def pay(self, order, security_code):
        print("Processing paypal payment...")
        print(f"Security code: {security_code}")
        order.status = "paid"
        
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = Paypal()
processor.pay(order, "1234-5678-9012-3456")