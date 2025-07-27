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
    def pay(self, order):
        pass

class Authorizer(ABC):
    @abstractmethod
    def is_verified(self) -> bool:
        pass

class SMSAUTH(Authorizer):
    verified = False

    def auth_sms(self, code):
        print(f"Authenticating SMS... {code}")
        self.verified = True

    def is_verified(self) -> bool:
        return self.verified
    

class DebitPay(Payment):
    def __init__(self, security_code, authorizer: Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer


    def pay(self, order):
        if not self.authorizer.is_verified():
            raise Exception("Payment not verified. Please authenticate first.")
        print("Processing debit payment...")
        print(f"Security code: {self.security_code}")
        order.status = "paid"

class CreditPay(Payment):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment...")
        print(f"Security code: {self.security_code}")
        order.status = "paid"

class PaypalPay(Payment):
    def __init__(self, email_address, authorizer: Authorizer):
        self.email_address = email_address
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_verified():
            raise Exception("Payment not verified. Please authenticate first.")
        print("Processing paypal payment...")
        print(f"Email Address: {self.email_address}")
        order.status = "paid"
        
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
authorizer = SMSAUTH()
processor = PaypalPay("ali@gmail.com", authorizer)
authorizer.auth_sms("123456")
processor.pay(order)