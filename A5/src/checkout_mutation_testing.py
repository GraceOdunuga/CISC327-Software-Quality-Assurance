import unittest
from user_profile import UserProfile
from restaurant import Restaurant

# For other functionalities, since check_out has some dependencies on other methods in shopping_cart.py.
class ShoppingCart:
    def __init__(self):
        self.cart = []

    # Add item from some restaurant by name
    def add_item(self, item, restaurant_name, quantity=1):
        for cart_item in self.cart:
            if cart_item.get(restaurant_name) != None: #check if the resaurant is in the cart
                if item['item_name'] in cart_item[restaurant_name]:
                    # If the item is already in the cart, update its quantity.
                    cart_item[restaurant_name][item['item_name']]['quantity'] += quantity
                    return "Item added to the cart."
                else:
                    # If the restaurant is in the cart but the item is not, add the item.
                    cart_item[restaurant_name][item['item_name']] = {
                        'quantity': quantity,
                        'price': item['price']
                    }
                    return "Cart updated."
                
        # If the restaurant is not in the cart, add it along with the item.
        self.cart.append({
            restaurant_name: {
                item['item_name']: {
                    'quantity': quantity,
                    'price': item['price']
                }
            }
        })      
        return "Cart updated.\n"
    
    # Remove item from some restaurant by name
    def remove_item(self, restaurant_name, item_name):
        for cart_item in self.cart:
            if cart_item.get(restaurant_name) is not None:
                if item_name in cart_item[restaurant_name]:
                    # If the item is found in the cart, remove it.
                    del cart_item[restaurant_name][item_name]
                    # If there are no more items for the restaurant, remove the restaurant from the cart.
                    if not cart_item[restaurant_name]:
                        self.cart.remove(cart_item)
                    return "Item removed from the cart."
        return "Item not found in the cart."
    
    # Cancel the order
    def cancel_order(self):
        self.cart = []

    # Calculate and return the price of all item's in the cart
    def cart_total_price(self):
        total_price = 0
        for cart_item in self.cart:
            for restaurant_name, items in cart_item.items():
                for item_name, details in items.items():
                    total_price += details['quantity'] * details['price']
        return total_price
        
    # Allows user to view all items that are in their cart.
    def view_cart(self):
        if not self.valid_item_quantity(len(self.cart)):
            return "Your shopping cart is empty."
            
        print("Your Shopping Cart:")
        for cart_item in self.cart:
            for restaurant_name, items in cart_item.items():
                for item_name, details in items.items():
                    print(f"{restaurant_name} - {item_name} ({details['quantity']} x ${details['price']:.2f})")
        print("")
    
    # Returns the cart. For testing purposes.
    def get_cart(self):
        return self.cart

    # Checks that the item quantity is a valid integer.
    def valid_item_quantity(self, quantity):
        return quantity > 0

# Decision mutation test #1
def check_out_decision1(shopping_cart, payment_methods, choice=None):
    if len(shopping_cart.cart) != 0: # MUTATION: changed == to !=
        print("Add items to cart to check out.\n")
        return
    user_cart_total = shopping_cart.cart_total_price()
    print(f"Total price in the cart: ${user_cart_total:.2f}")

    # check to make sure payment method has been added
    if len(payment_methods) == 0:
        print("No payment methods added. Return to main menu to add.")
        return

    card_number = payment_methods[0]['credit_card']
    print(f"Card on file: {card_number}")

    if choice == None:
        # Ask the user if they want to pay with the card on file
        choice = input("Do you wish to pay with this card? (yes/no): ")

    if choice.lower() != "yes":
        print("Order not placed. Returning to the main menu to update payment.")
        return "Order not placed. Returning to the main menu to update payment."
    shopping_cart.cancel_order()  # Clear the shopping cart after a successful order
    print("Payment successful. Order has been placed.")
    return "Payment successful. Order has been placed."

# Decision mutation test #2
def check_out_decision2(shopping_cart, payment_methods, choice=None):
    if len(shopping_cart.cart) == 0:
        print("Add items to cart to check out.\n")
        return
    user_cart_total = shopping_cart.cart_total_price()
    print(f"Total price in the cart: ${user_cart_total:.2f}")

    # check to make sure payment method has been added
    if len(payment_methods) != 0: # MUTATION: changed == to !=
        print("No payment methods added. Return to main menu to add.")
        return

    card_number = payment_methods[0]['credit_card']
    print(f"Card on file: {card_number}")

    if choice == None:
        # Ask the user if they want to pay with the card on file
        choice = input("Do you wish to pay with this card? (yes/no): ")

    if choice.lower() != "yes":
        print("Order not placed. Returning to the main menu to update payment.")
        return "Order not placed. Returning to the main menu to update payment."
    shopping_cart.cancel_order()  # Clear the shopping cart after a successful order
    print("Payment successful. Order has been placed.")
    return "Payment successful. Order has been placed."

# Decision mutation test #3
def check_out_decision3(shopping_cart, payment_methods, choice=None):
    if len(shopping_cart.cart) == 0:
        print("Add items to cart to check out.\n")
        return
    user_cart_total = shopping_cart.cart_total_price()
    print(f"Total price in the cart: ${user_cart_total:.2f}")

    # check to make sure payment method has been added
    if len(payment_methods) == 0:
        print("No payment methods added. Return to main menu to add.")
        return

    card_number = payment_methods[0]['credit_card']
    print(f"Card on file: {card_number}")

    if choice == None:
        # Ask the user if they want to pay with the card on file
        choice = input("Do you wish to pay with this card? (yes/no): ")

    if choice.lower() == "yes":  # MUTATION: changed != to ==
        print("Order not placed. Returning to the main menu to update payment.")
        return "Order not placed. Returning to the main menu to update payment."
    shopping_cart.cancel_order()  # Clear the shopping cart after a successful order
    print("Payment successful. Order has been placed.")
    return "Payment successful. Order has been placed."

# Value mutation test #1
def check_out_value1(shopping_cart, payment_methods, choice=None):
    if len(shopping_cart.cart) == 1: # MUTATION: added 1
        print("Add items to cart to check out.\n")
        return
    user_cart_total = shopping_cart.cart_total_price()
    print(f"Total price in the cart: ${user_cart_total:.2f}")

    # check to make sure payment method has been added
    if len(payment_methods) == 0:
        print("No payment methods added. Return to main menu to add.")
        return

    card_number = payment_methods[0]['credit_card']
    print(f"Card on file: {card_number}")

    if choice == None:
        # Ask the user if they want to pay with the card on file
        choice = input("Do you wish to pay with this card? (yes/no): ")

    if choice.lower() != "yes":
        print("Order not placed. Returning to the main menu to update payment.")
        return "Order not placed. Returning to the main menu to update payment."
    shopping_cart.cancel_order()  # Clear the shopping cart after a successful order
    print("Payment successful. Order has been placed.")
    return "Payment successful. Order has been placed."

# Value mutation test #2
def check_out_value2(shopping_cart, payment_methods, choice=None):
    if len(shopping_cart.cart) == 0:
        print("Add items to cart to check out.\n")
        return
    user_cart_total = shopping_cart.cart_total_price()
    print(f"Total price in the cart: ${user_cart_total:.2f}")

    # check to make sure payment method has been added
    if len(payment_methods) == 1: # MUTATION: added 1
        print("No payment methods added. Return to main menu to add.")
        return

    card_number = payment_methods[0]['credit_card']
    print(f"Card on file: {card_number}")

    if choice == None:
        # Ask the user if they want to pay with the card on file
        choice = input("Do you wish to pay with this card? (yes/no): ")

    if choice.lower() != "yes":
        print("Order not placed. Returning to the main menu to update payment.")
        return "Order not placed. Returning to the main menu to update payment."
    shopping_cart.cancel_order()  # Clear the shopping cart after a successful order
    print("Payment successful. Order has been placed.")
    return "Payment successful. Order has been placed."

# Statement mutation test #1
def check_out_statement1(shopping_cart, payment_methods, choice=None):
    if len(shopping_cart.cart) == 0:
        print("Add items to cart to check out.\n")
        return
    # user_cart_total = shopping_cart.cart_total_price() # MUTATION: delete this line
    print(f"Total price in the cart: ${user_cart_total:.2f}")

    # check to make sure payment method has been added
    if len(payment_methods) == 0:
        print("No payment methods added. Return to main menu to add.")
        return

    card_number = payment_methods[0]['credit_card']
    print(f"Card on file: {card_number}")

    if choice == None:
        # Ask the user if they want to pay with the card on file
        choice = input("Do you wish to pay with this card? (yes/no): ")

    if choice.lower() != "yes":
        print("Order not placed. Returning to the main menu to update payment.")
        return "Order not placed. Returning to the main menu to update payment."
    shopping_cart.cancel_order()  # Clear the shopping cart after a successful order
    print("Payment successful. Order has been placed.")
    return "Payment successful. Order has been placed."

# Statement mutation test #2
def check_out_statement2(shopping_cart, payment_methods, choice=None):
    if len(shopping_cart.cart) == 0:
        print("Add items to cart to check out.\n")
        return
    user_cart_total = shopping_cart.cart_total_price()
    print(f"Total price in the cart: ${user_cart_total:.2f}")

    # check to make sure payment method has been added
    if len(payment_methods) == 0:
        print("No payment methods added. Return to main menu to add.")
        return

    # card_number = payment_methods[0]['credit_card'] # MUTATION: delete this line
    print(f"Card on file: {card_number}")

    if choice == None:
        # Ask the user if they want to pay with the card on file
        choice = input("Do you wish to pay with this card? (yes/no): ")

    if choice.lower() != "yes":
        print("Order not placed. Returning to the main menu to update payment.")
        return "Order not placed. Returning to the main menu to update payment."
    shopping_cart.cancel_order()  # Clear the shopping cart after a successful order
    print("Payment successful. Order has been placed.")
    return "Payment successful. Order has been placed."

# Statement mutation test #3
def check_out_statement3(shopping_cart, payment_methods, choice=None):
    if len(shopping_cart.cart) == 0:
        print("Add items to cart to check out.\n")
        return
    user_cart_total = shopping_cart.cart_total_price()
    print(f"Total price in the cart: ${user_cart_total:.2f}")

    # check to make sure payment method has been added
    if len(payment_methods) == 0:
        print("No payment methods added. Return to main menu to add.")
        return

    card_number = payment_methods[0]['credit_card']
    print(f"Card on file: {card_number}")

    if choice == None:
        # Ask the user if they want to pay with the card on file
        choice = input("Do you wish to pay with this card? (yes/no): ")

    if choice.lower() != "yes":
        print("Order not placed. Returning to the main menu to update payment.")
        return "Order not placed. Returning to the main menu to update payment."
    # Clear the shopping cart after a successful order
    # shopping_cart.cancel_order()  # MUTATION: delete this line
    print("Payment successful. Order has been placed.")
    return "Payment successful. Order has been placed."

class TestApp(unittest.TestCase):
    def setUp(self):
        self.user = UserProfile("Test User", "test@test.com", "1234567890", "Test Address", "password123")
        self.payment_methods = [{
            "credit_card": "1111222233334444",
            "cvv": "111",
            "billing_address": "123 test street",
            "first_name": "Jill",
            "last_name": "Doe"
        }]
        self.restaurant = Restaurant("1", "Test Restaurant", "Test Address", "Test Category", "$$", "10:00 AM", "9:00 PM", {})
        self.cart = ShoppingCart()
        item1 = {"item_name": "Item1", "price": 10.0, "category": "food1", "description": "food1"}
        self.cart.add_item(item1, self.restaurant, 2)

    # Decision mutation test #1
    def test_decision_1(self):
        # Perform checkout, receive payment confirmation message
        payment_message = check_out_decision1(self.cart, self.payment_methods, "yes")

        # Assertions
        self.assertEqual(payment_message, "Payment successful. Order has been placed.")
        self.assertEqual(len(self.cart.cart), 0)  # Cart should be cleared after a successful order
    
    # Decision mutation test #2
    def test_decision_2(self):
        # Perform checkout, receive payment confirmation message
        payment_message = check_out_decision2(self.cart, self.payment_methods, "yes")

        # Assertions
        self.assertEqual(payment_message, "Payment successful. Order has been placed.")
        self.assertEqual(len(self.cart.cart), 0)  # Cart should be cleared after a successful order

    # Decision mutation test #3
    def test_decision_3(self):
        # Perform checkout, receive payment confirmation message
        payment_message = check_out_decision3(self.cart, self.payment_methods, "yes")

        # Assertions
        self.assertEqual(payment_message, "Payment successful. Order has been placed.")
        self.assertEqual(len(self.cart.cart), 0)  # Cart should be cleared after a successful order
    
    # Value mutation test #1
    def test_value_1(self):
        # Perform checkout, receive payment confirmation message
        payment_message = check_out_value1(self.cart, self.payment_methods, "yes")

        # Assertions
        self.assertEqual(payment_message, "Payment successful. Order has been placed.")
        self.assertEqual(len(self.cart.cart), 0)  # Cart should be cleared after a successful order

    # Value mutation test #2
    def test_value_2(self):
        # Perform checkout, receive payment confirmation message
        payment_message = check_out_value2(self.cart, self.payment_methods, "yes")

        # Assertions
        self.assertEqual(payment_message, "Payment successful. Order has been placed.")
        self.assertEqual(len(self.cart.cart), 0)  # Cart should be cleared after a successful order

    # Statement mutation test #1
    def test_statement_1(self):
        # Perform checkout, receive payment confirmation message
        payment_message = check_out_statement1(self.cart, self.payment_methods, "yes")

        # Assertions
        self.assertEqual(payment_message, "Payment successful. Order has been placed.")
        self.assertEqual(len(self.cart.cart), 0)  # Cart should be cleared after a successful order

    # Statement mutation test #2
    def test_statement_2(self):
        # Perform checkout, receive payment confirmation message
        payment_message = check_out_statement2(self.cart, self.payment_methods, "yes")

        # Assertions
        self.assertEqual(payment_message, "Payment successful. Order has been placed.")
        self.assertEqual(len(self.cart.cart), 0)  # Cart should be cleared after a successful order

    # Statement mutation test #3
    def test_statement_3(self):
        # Perform checkout, receive payment confirmation message
        payment_message = check_out_statement3(self.cart, self.payment_methods, "yes")

        # Assertions
        self.assertEqual(payment_message, "Payment successful. Order has been placed.")
        self.assertEqual(len(self.cart.cart), 0)  # Cart should be cleared after a successful order

if __name__ == '__main__':
    unittest.main()