# Creates and stores user information, including: name, email, phone number, address, password, and a list of all payment methods added.
# Contains functions for modifying profile information, and adding/removing/modifying payment methods.

class UserProfile:
    def __init__(self, name, email, phone_number, address, password, payment_methods=[]):
        if self.valid_credentials(email, phone_number, password):
            self.name = name
            self.email = email
            self.phone_number = phone_number
            self.address = address
            self.password = password
            self.payment_methods = payment_methods
        else:
            self.name = None
            self.email = None
            self.phone_number = None
            self.address = None
            self.password = None
            self.payment_methods = []

    # Validate email, phone number & password
    def valid_credentials(self, email, phone_number, password):
        if "@" not in email:
            print("Invalid email. Please try again.\n")
            return False

        # phone number must be of length 10 and all digits
        if len(phone_number) != 10 or not phone_number.isdigit():
            print("Invalid phone number. Please try again.\n")
            return False
        
        # password must be 8 characters
        if len(password) < 8:
            print("Password too short. Please try again.\n")
            return False
        
        return True

    # Add a payment method for user
    def add_payment(self, payment_info):
        self.payment_methods.append({
            "credit_card": payment_info["credit_card"],
            "cvv": payment_info["cvv"],
            "billing_address": payment_info["billing_address"],
            "card_name": payment_info["first_name"] + " " + payment_info["last_name"]
        })
        return "Payment method added."
    
    # Remove a payment method by id in list for user
    def remove_payment(self, id):
        self.payment_methods.pop(id)
        return "Payment method removed."

    # Modify a payment method by id in list for user
    def modify_payment(self, id, payment_info):
        self.payment_methods[id] = ({
            "credit_card": payment_info["credit_card"],
            "cvv": payment_info["cvv"],
            "billing_address": payment_info["billing_address"],
            "card_name": payment_info["first_name"] + payment_info["last_name"]
        })
        return "Payment method modified."

    # Display all payment methods for user
    def show_payments(self):
        if len(self.payment_methods) == 0:
            print("No payment methods found.")
            return
        
        for payment in self.payment_methods:
            print(f"Credit card: {payment['credit_card']}      Name on card: {payment['card_name']}       Billing address: {payment['billing_address']}")

    # Modify profile information for user
    def modify_profile(self, email, phone_number, address, new_password):
        if self.valid_credentials(email, phone_number, new_password):
            self.email = email
            self.phone_number = phone_number
            self.address = address
            self.password = new_password
            return True
        return False

    # Show profile information of user
    def show_profile(self):
        print(f"Name: {self.name}       Email: {self.email}        Address: {self.address}     Phone Number: {self.phone_number}\n")
    
    # Returns profile in dict format for storing in DB
    def get_profile(self):
        profile_data = {
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number,
            "address": self.address,
            "password": self.password,
            "payment_methods": self.payment_methods
        }
        return profile_data

    # Validate login of user
    def login(self, email, password):
        if self.password == password and self.email == email:
            return "You have logged in successfully."
        else:
            return "Invalid email or password. Please try again."