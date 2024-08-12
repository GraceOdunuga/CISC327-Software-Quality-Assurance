# Import necessary modules and classes
from shopping_cart import ShoppingCart
from restaurant import Restaurant
from user_profile import UserProfile
import pymongo

# Function to validate user credentials
def valid_credentials(phone_number, email, password):
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
            print('bruh')
            return False
        
        return True

# Function to register a new user
def register():
    while True:
        name = input("Enter your name: ")
        phone_number = input("Enter your phone number: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        password = input("Choose a password (must be at least 8 characters): ")
        if valid_credentials(phone_number, email, password):
            user_data = { # arrange data into row format
                "name": name,
                "phone_number": phone_number,
                "email": email,
                "address": address,
                "password": password,
                "payment_methods": []    
            }
            new_insert = users_table.insert_one(user_data) # add row to table
            users.append((UserProfile(name, email, phone_number, address, password), new_insert.inserted_id))
            
            print("Account created for " + name +". Please login.\n")
            break
        else: # allow user to exit to main menu after incorrect registration attempt
            exit_check = input("Enter 'r' to retry registration, anything else to exit: ")
            if exit_check != 'r':
                break

# Function to log in a user
def login():
    if len(users) == 0: # empty users table
        return print("Please register first.")
        
    while True:
        # allow user to exit to main menu after incorrect login attempt
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        for user in users:
            user_info = user[0]
            if user_info.email == email and user_info.password == password:
                print("You have logged in successfully.")
                return user
        else:
            print("Invalid email or password. Please try again.")
        
        # allow user to exit to main menu after incorrect login attempt
        exit_check = input("Enter 'r' to retry login, anything else to exit: ")
        if exit_check != 'r':
            break

# Function to modify the user's profile
def modify_profile():
    while True:
        phone_number = input("Enter your new phone number: ")
        email = input("Enter your new email: ")
        address = input("Enter your new address: ")
        old_password = input("Enter your old password: ")
        new_password = input("Choose a new password (must be at least 8 characters): ")

        if valid_credentials(phone_number, email, new_password) and old_password == cur_profile[0].password:
            cur_profile[0].modify_profile(email, phone_number, address, new_password)

            # update profile in database with modified profile info
            
            users_table.update_one(
                {"_id": cur_profile[1]},
                {"$set": cur_profile[0].get_profile()}
            )
            print("Profile information changed successfully.\n")
            break
        else:
            print("Invalid password. Please try again.")
            # allow user to exit to main menu after incorrect password attempt
            exit_check = input("Enter 'r' to retry password, anything else to exit: ")
            if exit_check != 'r':
                break

def show_profile():
    cur_profile[0].show_profile()

# Function to add a payment method to the current user's profile
def add_payment():
    credit_card = input("Enter your credit card numbers: ")
    cvv = input("Enter your cvv: ")
    first_name = input("Enter the first name on the card: ")
    last_name = input("Enter the last name on the card: ")
    billing_address = input("Enter the billing address on the card: ")
    payment_info = {
        "credit_card": credit_card,
        "cvv": cvv,
        "billing_address": billing_address,
        "first_name": first_name,
        "last_name": last_name
    }
    cur_profile[0].add_payment(payment_info)

    # update profile in database with new payment info
    update_payment_db()
    print("Payment method added.\n")

# Function to modify an existing payment method
def modify_payment():
    while True:
        id = int(input("Enter the id of the payment method to modify: "))
        if id >= len(cur_profile[0].payment_methods) or id < 0:
            print("Invalid id. Please try again.")
            # allow user to exit to main menu after incorrect id attempt
            exit_check = input("Enter 'r' to retry id, anything else to exit: ")
            if exit_check != 'r':
                break
        else:
            credit_card = input("Enter your credit card numbers: ")
            cvv = input("Enter your cvv:")
            billing_address = input("Enter the billing address on the card: ")
            first_name = input("Enter the first name on the card: ")
            last_name = input("Enter the last name on the card:")

            payment_info = {
                "credit_card": credit_card,
                "cvv": cvv,
                "billing_address": billing_address,
                "first_name": first_name,
                "last_name": last_name
            }

            cur_profile[0].modify_payment(id, payment_info)

            # update profile in database with modified payment info
            update_payment_db()
            print("Payment method modified.\n")
            break

# Function to remove payment method
def remove_payment():
    while True:
        id = int(input("Enter the id of the payment method to remove: "))
        if id >= len(cur_profile[0].payment_methods) or id < 0:
            print("Invalid id. Please try again.")
            # allow user to exit to main menu after incorrect id attempt
            exit_check = input("Enter 'r' to retry id, anything else to exit: ")
            if exit_check != 'r':
                break
        else:
            cur_profile[0].remove_payment(id)
            # update profile in database with removed payment info
            update_payment_db()
            print("Payment method removed.\n")
            break

# Function to update payment methods in backend database (adding, modifying, & removing payments)
def update_payment_db():
    users_table.update_one(
        {"_id": cur_profile[1]},
        {"$set": cur_profile[0].get_profile()}
    )

# Function to show all payment methods for logged in user
def show_payments():
    cur_profile[0].show_payments()

# Function to view the list of available restaurants
def view_restaurants():
    print("\nList of available restaurants:")

    for restaurant in restaurants:
        print(restaurant.name)
    print("")

# Function to view the menu of a specific restaurant
def view_menu():
    restaurant_name = input("Enter the restaurant you wish to see the menu: ")

    for restaurant in restaurants:
        if restaurant_name == restaurant.name:
            restaurant.show_menu()
            return
    print("Restaurant not found.\n")

# Function to add an item to the shopping cart
def add_to_cart():
    restaurant_name = input("Enter the restaurant where you want to add items: ")
    item_name = input("Enter the name of the item to add to the cart: ")
    quantity = int(input("Enter the quantity: "))

    for restaurant in restaurants:
        if restaurant.name == restaurant_name:
            for item in restaurant.menu.keys():
                if item == item_name:
                    user_cart.add_item(restaurant.menu[item], restaurant.name, quantity)
                    print("Item added to the cart.\n")
                    return "Item added to the cart."
    print("Restaurant or item not found.")
    return "Restaurant or item not found."

# Function to remove an item from the shopping cart
def remove_from_cart():
    restaurant_name = input("Enter the restaurant where you want to remove an item from the cart: ")
    item_name = input("Enter the name of the item to remove from the cart: ")
    
    result = user_cart.remove_item(restaurant_name, item_name)
    
    if result == "Item removed from the cart.":
        print(result)
    else:
        print("Item not found in the cart.")

# Function to view the contents of the shopping cart
def view_cart():
    user_cart.view_cart()

# Function to check out and complete the order
def check_out():
    user_cart.check_out(cur_profile[0].payment_methods)

# Function to print the menu options for a logged-in user
def print_options():
    print(f"Hello {cur_profile[0].name}. Please choose one of the options below.")
    print("1. View restaurants")
    print("2. View restaurant menu")
    print("3. Add item to cart")
    print("4. Remove item from cart")
    print("5. View cart")
    print("6. Check out")
    print("7. Cancel/withdraw current order")
    print("8. Logout")
    print("9. Display profile information")
    print("10. Modify profile information")
    print("11. Modify payment methods")
    print("0. Exit")

# Create a shopping cart for the current user
user_cart = ShoppingCart()

# Initialize the current user profile as None (no user logged in)
cur_profile = None

# Access MongoDB database
mongo_url = 'mongodb+srv://group24:eyljlgY1EkNeE8AB@group24-project.rv8qyhx.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(mongo_url)
db = client['backend-database'] # database

# Load all users from DB into a list
users_table = db['users'] # users table
users = []
users_list = list(users_table.find())
for user in users_list:
    users.append((UserProfile(
        user['name'],
        user['email'],
        user['phone_number'],
        user['address'],
        user['password'],
        user['payment_methods']
    ), user['_id']))

# Load all restaurants from DB into a list
restaurants_table = db['restaurants'] # restaurants table
restaurants = []
restaurant_list = list(restaurants_table.find())
for restaurant in restaurant_list:
    restaurants.append(Restaurant(
        restaurant['id_num'], 
        restaurant['name'],
        restaurant['address'],
        restaurant['category'],
        restaurant['price_range'],
        restaurant['open_time'],
        restaurant['close_time'],
        restaurant['menu']
    ))

# Main application loop
while True:
    if cur_profile is None:  # If no user is logged in
        print("Hello, welcome to our delivery app. Please choose one of the options below.")
        print("0: Register")
        print("1: Login")
        print("2: Exit")
        user_choice = input("Enter choice: ")
        if user_choice == "0":
            register()
        elif user_choice == "1":
            cur_profile = login()
        elif user_choice == "2":
            print("Application exited.")
            break
        else:
            print("Invalid input. Please try again.")
    else:
        print_options()
        choice = input("Enter the number of your choice: ")
        # Handle user choices based on the selected option

        if choice == "1":
            view_restaurants()
        elif choice == "2":
            view_menu()
        elif choice == "3":
            add_to_cart()
        elif choice == "4":
            remove_from_cart()
        elif choice == "5":
            cart_status = view_cart()
            if cart_status:
                print(cart_status)
            else:
                print("Empty cart.")
        elif choice == "6":
            check_out()
        elif choice == "7":
            user_cart = []
            print("Cart is now empty.")
        elif choice == "8":
            cur_profile = None
            print("You have logged out.\n")
        elif choice == "9":
            show_profile()
        elif choice == "10":
            modify_profile()
        elif choice == "11":
            print(f"\nPlease choose one of the options below.")
            print("0: Add payment method")
            print("1: Modify payment method")
            print("2: Remove payment method")
            print("3: Show all payment methods")
            user_choice = input("Enter choice: ")
            if user_choice == "0":
                add_payment()
            elif user_choice == "1":
                modify_payment()
            elif user_choice == "2":
                remove_payment()
            elif user_choice == "3":
                show_payments()
            else:
                print("Invalid option return to main menu")
        elif choice == "0":
            print("Thank you for using our app. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
    print("")
