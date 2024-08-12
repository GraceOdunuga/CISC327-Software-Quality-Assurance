# Import necessary modules and classes
from restaurant import Restaurant, restaurants_all
from shopping_cart import ShoppingCart
from menu import RestaurantMenu, Item
from profile_manager import UserProfile

# Create a shopping cart for the current user
user_cart = ShoppingCart()

# Initialize an empty list to store user profiles
profiles = []

# Initialize the current user profile as None (no user logged in)
cur_profile = None

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
            profiles.append(UserProfile(address, phone_number, name, email, password))
            break

# Function to log in a user
def login():
    if not profiles:  # Check if there are no user profiles
        return print("Please register first")
        
    while True:
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        for p in profiles:
            if p.login(email, password):
                print(f"You have logged in successfully.\n")
                return p
        print("Invalid email or password. Please try again.\n")

# Function to modify the user's profile
def modify_profile():
    while True:
        phone_number = input("Enter your new phone number: ")
        email = input("Enter your new email: ")
        address = input("Enter your new address: ")
        old_password = input("Enter your old password: ")
        new_password = input("Choose a new password (must be at least 8 characters): ")
        if valid_credentials(phone_number, email, new_password):
            cur_profile.modify_profile(address, phone_number, email, old_password, new_password)
            break

# Function to add a payment method to the current user's profile
def add_payment():
    cc = input("Enter your credit card information: ")
    name = input("Enter the name on the card: ")
    address = input("Enter the address on the card: ")
    cur_profile.payment_manager.add_payment(cc, name, address)

# Function to modify an existing payment method
def modify_payment():
    id = int(input("Enter the id of the payment method to modify: "))
    cc = input("Enter your credit card information: ")
    name = input("Enter the name on the card: ")
    address = input("Enter the address on the card: ")
    cur_profile.payment_manager.modify_payment(id, cc, name, address)

# Function to view the list of available restaurants
def view_restaurants():
    print("List of available restaurants:")
    for restaurant in restaurants_all:
        print(restaurant.name)

# Function to view the menu of a specific restaurant
def view_menu():
    restaurant_name = input("Enter the restaurant you wish to see the menu: ")
    for restaurant in restaurants_all:
        if restaurant.name == restaurant_name:
            restaurant.show_menu()
            return
    print("Restaurant not found.")

# Function to add an item to the shopping cart
def add_to_cart():
    restaurant_name = input("Enter the restaurant where you want to add items: ")
    item_name = input("Enter the name of the item to add to the cart: ")
    quantity = int(input("Enter the quantity: "))
    
    for restaurant in restaurants_all:
        if restaurant.name == restaurant_name:
            for item in restaurant.menu.items:
                if item.name == item_name:
                    user_cart.add_item(item, restaurant, quantity)
                    print("Item added to the cart.")
                    return
    print("Restaurant or item not found.")

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
    user_cart_total = user_cart.cart_total_price()
    print(f"Total price in the cart: ${user_cart_total:.2f}")
    #show card number i will add logic later
    card_number = cur_profile.payment_manager.id
    print(f"Card on file: {card_number}")

    # Ask the user if they want to pay with the card on file
    choice = input("Do you wish to pay with this card? (yes/no): ")

    if choice.lower() == "yes":
        print("Payment successful. Order has been placed.")
        user_cart.cancel_order()  # Clear the shopping cart after a successful order
    else:
        print("Order not placed. Returning to the main menu to update payment.")

# Function to print the menu options for a logged-in user
def print_options():
    print(f"Hello {cur_profile.name}. Please choose one of the options below.")
    print("1. View restaurants")
    print("2. View restaurant menu")
    print("3. Add item to cart")
    print("4. Remove item from cart")
    print("5. View order details")
    print("6. Check out")
    print("7. Logout")
    print("8. Display profile information")
    print("9. Modify profile information")
    print("10. Modify payment methods")
    print("11 Show all orders")
    print("12 Withdraw current order")
    print("0. Exit")


# Main application loop
while True:
    if cur_profile is None:  # If no user is logged in
        print("Hello, welcome to our delivery app. Please choose one of the options below.")
        print("0: Register")
        print("1: Login")
        print("2: Exit")
        num = int(input("Enter choice: "))
        if num == 0:
            register()
        elif num == 1:
            cur_profile = login()
        elif num == 2:
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
            view_cart()
        elif choice == "6":
            check_out()
        elif choice == "7":
            cur_profile = None
            print("You have logged out.\n")
        elif choice == "8":
            cur_profile.show_profile()
        elif choice == "9":
            modify_profile()
        elif choice == "10":
            print(f"\nPlease choose one of the options below.")
            print("0: Add payment method")
            print("1: Remove payment method")
            print("2: Modify payment method")
            print("3: Show all payment methods")
            num = (int)(input("Enter choice: "))
            if num == 0:
                add_payment()
            elif num == 1:
                modify_payment()
            elif num == 2:
                id = int(input("Enter the id of the payment method to remove:"))
                cur_profile.payment_manager.remove_payment(id)
            elif num == 3:
                    cur_profile.payment_manager.show_payments()
            else:
                print("Invalid option return to main menu")
        elif choice == "11":
            user_cart = []
        elif choice == "0":
            print("Thank you for using our app. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")





