import unittest
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        # Initialize a ShoppingCart instance for each test
        self.shopping_cart = ShoppingCart()

    def test_add_item_nonexistent_restaurant(self):
        item = {"item_name": "Salad", "price": 8.99}
        restaurant = "Nonexistent Restaurant"
        quantity = 1

        result = self.shopping_cart.add_item(item, restaurant, quantity)

        self.assertEqual(result, "Restaurant not found.")

    def test_add_item_invalid_quantity(self):
        item = {"item_name": "Cheesy Morning Fries", "price": 6.59}
        restaurant = "Bunrise Burgers"
        quantity = -1

        result = self.shopping_cart.add_item(item, restaurant, quantity)

        self.assertEqual(result, "Invalid item quantity.")

    def test_add_item_existing_item(self):
        item = {"item_name": "Cheesy Morning Fries", "price": 6.59}
        restaurant = "Bunrise Burgers"
        quantity = 1

        # Add item to cart before testing
        self.shopping_cart.add_item(item, restaurant, quantity)

        result = self.shopping_cart.add_item(item, restaurant, quantity)

        self.assertEqual(result, "Item added to the cart.")

    def test_add_item_new_item(self):
        item = {"item_name": "Classic Bunrise Burger", "price": 8.79}
        restaurant = "Bunrise Burgers"
        quantity = 2

        result = self.shopping_cart.add_item(item, restaurant, quantity)

        self.assertEqual(result, "Cart updated.\n")

    def test_add_item_new_restaurant(self):
        item = {"item_name": "Lobster Tortellini", "price": 18.0}
        restaurant = "Ocean Restaurant"
        quantity = 1

        result = self.shopping_cart.add_item(item, restaurant, quantity)

        self.assertEqual(result, "Cart updated.\n")

if __name__ == '__main__':
    unittest.main()
