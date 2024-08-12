# Class to represent a payment method
class PaymentMethod:
    def __init__(self, id, cc, name, address):
        self.id = id
        self.cc = cc
        self.name = name
        self.address = address

# Class to manage payment methods
class PaymentManager:
    def __init__(self):
        self.payment_methods = []
        self.id = 0

    # Method to add a new payment method
    def add_payment(self, cc, name, address):
        payment_method = PaymentMethod(self.id, cc, name, address)
        self.payment_methods.append(payment_method)
        print(f"Payment method added with id {self.id}.\n")
        self.id += 1

    # Method to remove a payment method by ID
    def remove_payment(self, id):
        self.payment_methods.pop(id)
        print(f"Payment method with id {id} removed.\n")

    # Method to modify a payment method by ID
    def modify_payment(self, id, cc, name, address):
        if id >= len(self.payment_methods) or id < 0:
            print("Invalid id. Please try again.")
            return
        payment = self.payment_methods[id]
        payment.cc = cc
        payment.name = name
        payment.address = address
        print(f"Payment method modified.\n")

    # Method to display all payment methods
    def show_payments(self):
        if len(self.payment_methods) == 0:
            print("No payment methods are in the system for your account.\n")
            return

        print("--------------------------------------------------------------------------------------------------------------\nPayment Methods:")
        for payment in self.payment_methods:
            print(f"ID: {payment.id}        CC: {payment.cc}        Name: {payment.name}        Address: {payment.address}")
        print("--------------------------------------------------------------------------------------------------------------\n")

# Example usage:
# payments = PaymentManager()
# payments.add_payment("1111222233334444", "Bob", "999 Bob Street")
# payments.show_payments()
# payments.remove_payment(0)
# payments.show_payments()
