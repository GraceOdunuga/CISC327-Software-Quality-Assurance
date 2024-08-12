from payment_methods import PaymentManager

class UserProfile:
    def __init__(self, address, phone_number, name, email, password):
        self.address = address
        self.phone_number = phone_number
        self.name = name
        self.password = password
        self.email = email
        self.payment_manager = PaymentManager()
        print("Account created. Please login.\n")
    
    def valid_credentials(self, phone_number, email, password):
        # phone number must be of length 10 and all digits
        if len(phone_number) != 10 or not phone_number.isdigit():
            print("Invalid phone number. Please try again.\n")
            return False
        
        # password must be 8 characters
        if len(password) < 8:
            print("Password too short. Please try again.\n")
            return False
        
        if "@" not in email:
            print("Invalid email. Please try again.\n")
            return False
        
        return True
    
    def modify_profile(self, address, phone_number, email, old_password, new_password):
        if self.password == old_password:
            if self.valid_credentials(phone_number, email, new_password):
                self.address = address
                self.phone_number = phone_number
                self.email = email
                self.password = new_password
                print(f"Your profile information has been changed.\n")
        else:
            print("Password does not match old password. Please try again.\n")
        
    def show_profile(self):
        print(f"Name: {self.name}       Email: {self.email}        Address: {self.address}     Phone Number: {self.phone_number}\n")
    
    def login(self, email, password):
        if self.password == password and self.email == email:
            return True
        else:
            return False

# Example usage:
#     bob = UserProfile("999 Bob Street", "1112223333", "Bob", "bob@gmail.com", "password123")
#     bob.show_profile()
#     bob.modify_profile("888 Bob Street", "2223334444", "bob2@gmail.com", "password124", "password321")
#     bob.show_profile()
#     bob.modify_profile("888 Bob Street", "2223334444", "bob2@gmail.com", "password123", "password321")
#     bob.show_profile()