# Creates and stores a shopping cart for the user.
# Contains functions for adding/removing items to the cart, as well as canceling the order, checking out, and viewing the cart.

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

    # Place the order / check out. Checks for payment info, and prompts user to complete checkout.
    def check_out(self, payment_methods, choice=None):
        if len(self.cart) == 0:
            print("Add items to cart to check out.\n")
            return
        user_cart_total = self.cart_total_price()
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
        self.cancel_order()  # Clear the shopping cart after a successful order
        print("Payment successful. Order has been placed.")
        return "Payment successful. Order has been placed."
        
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
