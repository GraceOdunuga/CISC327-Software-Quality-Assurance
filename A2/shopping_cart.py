from restaurant import Restaurant
from menu import Item, RestaurantMenu

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, item, restaurant, quantity=1):

        #test in next assignment
        # if self.is_valid_restaurant(restaurant, self.restaurants_all):
        #     return "Restaurant not found in the master list."
        
        # if self.is_valid_item(item, restaurant):
        #    return "Restaurant not found in the master list."

        for cart_item in self.cart:
            if cart_item.get(restaurant.name) != None: #check if the resaurant is in the cart
                if item.name in cart_item[restaurant.name]:
                    # If the item is already in the cart, update its quantity.
                    cart_item[restaurant.name][item.name]['quantity'] += quantity
                    return "Cart updated."
                else:
                    # If the restaurant is in the cart but the item is not, add the item.
                    cart_item[restaurant.name][item.name] = {
                        'quantity': quantity,
                        'price': item.price
                    }
                    return "Cart updated."
                
        # If the restaurant is not in the cart, add it along with the item.
        self.cart.append({
            restaurant.name: {
                item.name: {
                    'quantity': quantity,
                    'price': item.price
                }
            }
        })      
        return "Cart updated."
    
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
    
    def cancel_order(self):
        self.cart = []

    def cart_total_price(self):
            total_price = 0
            for cart_item in self.cart:
                for restaurant_name, items in cart_item.items():
                    for item_name, details in items.items():
                        total_price += details['quantity'] * details['price']
            return total_price
    
    def view_cart(self):
        if not self.cart:
            print("Your shopping cart is empty.")
            return

        print("Your Shopping Cart:")
        for cart_item in self.cart:
            for restaurant_name, items in cart_item.items():
                for item_name, details in items.items():
                    print(f"{restaurant_name} - {item_name} ({details['quantity']} x ${details['price']:.2f})")


