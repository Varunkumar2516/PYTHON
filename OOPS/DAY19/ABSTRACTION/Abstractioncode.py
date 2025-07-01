from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class PayPal(PaymentGateway):
    def pay(self, amount):
        # complex logic hidden from user
        print(f"Paid ₹{amount} using PayPal")

class Stripe(PaymentGateway):
    def pay(self, amount):
        # different logic, still hidden
        print(f"Paid ₹{amount} using Stripe")

# User just interacts like this:
payment = PayPal()
payment.pay(500)

newpayment=Stripe()
newpayment.pay(1000)

#until we dont override the abstract method pay() we cannot inherit that class
"""
Whats Hidden?
1.API requests
2.Security tokens
3.Error handling
4.Payment verification
User doesnt care. They only need to call .pay(amount)."""