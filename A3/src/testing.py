from user_profile import UserProfile
from shopping_cart import ShoppingCart
from restaurant import Restaurant
import unittest


# Helper function: to view the list of available restaurants
def view_restaurants(restaurants):
    restaurant_list = [restaurant.name for restaurant in restaurants]
    return restaurant_list


class TestApp(unittest.TestCase):
    def setUp(self):
        # Initialize any necessary objects or data before each test
        self.user = UserProfile("Test Address", "1234567890", "Test User", "test@test.com", "password123")
        self.cart = ShoppingCart()
        self.restaurant = Restaurant("1", "Test Restaurant", "Test Address", "Test Category", "$$", "10:00 AM", "9:00 PM", {})
        self.restaurants = [
            Restaurant("1", "Restaurant A", "Address A", "Category A", "$$", "10:00 AM", "9:00 PM", {}),
            Restaurant("2", "Restaurant B", "Address B", "Category B", "$$", "11:00 AM", "8:00 PM", {}),
            Restaurant("3", "Restaurant C", "Address C", "Category C", "$", "9:00 AM", "10:00 PM", {})
        ]

    def test_add_payment(self):
        # Test adding payment method
        payment_info = {
            "credit_card": "1111222233334444",
            "cvv": "111",
            "billing_address": "1 Queen St",
            "first_name": "John",
            "last_name": "Doe"
        }
        message = self.user.add_payment(payment_info)
        self.assertEqual(message, "Payment method added.")

    def test_remove_payment(self):
        # Test removing a payment method
        self.user.add_payment({
            "credit_card": "1111222233334444",
            "cvv": "111",
            "billing_address": "1 Queen St",
            "first_name": "John",
            "last_name": "Doe"
        })
        message = self.user.remove_payment(0)
        self.assertEqual(message, "Payment method removed.")

    def test_modify_payment(self):
        # Add a payment method
        self.user.add_payment({
            "credit_card": "1111222233334444",
            "cvv": "111",
            "billing_address": "1 Queen St",
            "first_name": "John",
            "last_name": "Doe"
        })

        # Modify the payment method
        modified_payment_info = {
            "credit_card": "5555666677778888",
            "cvv": "222",
            "billing_address": "2 King St",
            "first_name": "Jane",
            "last_name": "Smith"
        }

        message = self.user.modify_payment(0, modified_payment_info)
        self.assertEqual(message, "Payment method modified.")

    def test_check_out(self):
        # Set the current user profile to the test user
        cur_profile = self.user
        cur_profile.add_payment({
            "credit_card": "1111222233334444",
            "cvv": "111",
            "billing_address": "123 test street",
            "first_name": "Jill",
            "last_name": "Doe"
        })

        # Add items to the shopping cart
        item1 = {"item_name": "Item1", "price": 10.0, "category": "food1", "description": "food1"}
        item2 = {"item_name": "Item2", "price": 5.0, "category": "food2", "description": "food2"}

        self.cart.add_item(item1, self.restaurant, 2)
        self.cart.add_item(item2, self.restaurant, 3)

        # Perform the checkout
        payment_message = self.cart.check_out(cur_profile.payment_methods, "yes")

        # Assertions
        self.assertEqual(payment_message, "Payment successful. Order has been placed.")
        self.assertEqual(len(self.cart.cart), 0)  # Cart should be cleared after a successful order

    def test_modify_profile(self):
        # Initialize a test user profile
        test_user = UserProfile("Test User", "test@test.com", "1234567890", "Test Address", "password123")
        
        # Modify the profile information
        new_phone_number = "9876543210"
        new_email = "newemail@test.com"
        new_address = "New Address"
        old_password = "password123"
        new_password = "newpassword123"
        
        # Ensure old password is same as stored one
        self.assertEqual(test_user.password, old_password)

        # Ensure new profile information meets criteria
        result = test_user.valid_credentials(new_email, new_phone_number, new_password)
        self.assertTrue(result)

        # Modify profile
        test_user.modify_profile(new_email, new_phone_number, new_address, new_password)
        
        # Check if the profile information is modified
        self.assertEqual(test_user.phone_number, new_phone_number)
        self.assertEqual(test_user.email, new_email)
        self.assertEqual(test_user.address, new_address)
        self.assertEqual(test_user.password, new_password)

    def test_user_registration(self):
        # Initialize a test user profile
        
        valid_name = "Test User"
        valid_phone_number = "1234567890"
        valid_email = "test@test.com"
        valid_address = "Test Address"
        valid_password = "password123"

        # Test valid user registration
        test_user = UserProfile(valid_name, valid_email, valid_phone_number, valid_address, valid_password)
                
        # Check if the registration was successful
        self.assertEqual(test_user.name, valid_name)
        self.assertEqual(test_user.phone_number, valid_phone_number)
        self.assertEqual(test_user.email, valid_email)
        self.assertEqual(test_user.address, valid_address)
        self.assertEqual(test_user.password, valid_password)

        # Test invalid user registration (e.g., invalid phone number)
        invalid_name = "Invalid User"
        invalid_email = "invalid_email.com"
        invalid_phone_number = "invalid"
        invalid_address = "Invalid Address"
        invalid_password = "short"

        # Test invalid user registration
        invalid_test_user = UserProfile(invalid_name, invalid_email, invalid_phone_number, invalid_address, invalid_password)
                
        # Check if the registration fails with invalid inputs
        self.assertNotEqual(invalid_test_user.name, invalid_name)
        self.assertNotEqual(invalid_test_user.email, invalid_email)
        self.assertNotEqual(invalid_test_user.phone_number, invalid_phone_number)
        self.assertNotEqual(invalid_test_user.address, invalid_address)
        self.assertNotEqual(invalid_test_user.password, invalid_password)

    def test_user_login_valid(self):
        # Initialize a test user profile
        test_user = UserProfile("Test User", "test@test.com", "1234567890", "Test Address", "password123")
        
        # Test valid user login
        valid_email = "test@test.com"
        valid_password = "password123"
        
        login_result = test_user.login(valid_email, valid_password)
        
        # Check if the login is successful
        self.assertEqual(login_result, "You have logged in successfully.")

    def test_user_login_invalid(self):
        # Initialize a test user profile
        test_user = UserProfile("Test User", "test@test.com", "1234567890", "Test Address", "password123")
        
        # Test invalid user login with incorrect email
        invalid_email = "invalid_email@test.com"
        valid_password = "password123"
        
        login_result = test_user.login(invalid_email, valid_password)
        
        # Check if the login fails with incorrect email
        self.assertEqual(login_result, "Invalid email or password. Please try again.")

        # Test invalid user login with incorrect password
        valid_email = "test@test.com"
        invalid_password = "incorrect_password"
        
        login_result = test_user.login(valid_email, invalid_password)
        
        # Check if the login fails with incorrect password
        self.assertEqual(login_result, "Invalid email or password. Please try again.")

    def test_view_restaurants(self):
        # Get all restaurants
        restaurants = view_restaurants(self.restaurants)
        print(restaurants)

        # Check list of restaurants matches expected result
        expected_restaurants = ["Restaurant A", "Restaurant B", "Restaurant C"]
        self.assertEqual(restaurants, expected_restaurants)
        
        # Create a new restaurant with a menu
        some_menu = {
            "hamburger": {
                "name": "Hamburger",
                "category": "American",
                "description": "American Hamburger with bun",
                "price": 7.99
            }
        }
        new_restaurant = Restaurant("1", "Restaurant D", "Address D", "Category D", "$$$", "8:00 AM", "10:00 PM", some_menu)

        # Call show menu
        menu_message = new_restaurant.show_menu()

        # Expected message
        expected_message = "Hamburger - 7.99\n"

        # Check if the menu matches the expected result
        self.assertEqual(expected_message, menu_message)
    
    def test_add_to_cart(self):
        # Create a test cart
        cart = ShoppingCart()

        # Create a test item and restaruant name
        restaurant_name = "Amazing Restaurant"
        item = {
            "item_name": "Item1",
            "category": "Some",
            "description": "Filler",
            "price": 2
        }

        # Add item to the cart
        cart.add_item(item, restaurant_name)

        # Get shopping cart
        cart_after = cart.get_cart()

        # Expected cart
        expected_cart = [
            {"Amazing Restaurant": {
                "Item1": {
                    "quantity": 1,
                    "price": 2
                }
            }}
        ]

        # Check to make sure cart is as expected
        self.assertEqual(cart_after, expected_cart)

    def test_remove_from_cart(self):
        # Create a test cart
        cart = ShoppingCart()

        # Create a test item and restaruant name
        restaurant_name = "Amazing Restaurant"
        item = {
            "item_name": "Item1",
            "category": "Some",
            "description": "Filler",
            "price": 2
        }

        # Add item to the cart
        cart.add_item(item, restaurant_name)

        # Remove item from cart
        cart.remove_item(restaurant_name, item["item_name"])

        # Get shopping cart
        cart_after = cart.get_cart()

        # Check to make sure cart is as expected (empty)
        self.assertEqual(cart_after, [])

    def test_cancel_order(self):
        # Create a test cart
        cart = ShoppingCart()

        # Create a test item and restaruant name
        restaurant_name = "Amazing Restaurant"
        item = {
            "item_name": "Item1",
            "category": "Some",
            "description": "Filler",
            "price": 2
        }

        # Add item to the cart
        cart.add_item(item, restaurant_name)

        # Clear cart
        cart.cancel_order()

        # Get shopping cart
        cart_after = cart.get_cart()

        # Check to make sure cart is as expected (empty)
        self.assertEqual(cart_after, [])

    def test_cart_total_price(self):
        # Create a test cart
        cart = ShoppingCart()

        # Create a test item and restaruant name
        restaurant_name = "Amazing Restaurant"
        item = {
            "item_name": "Item1",
            "category": "Some",
            "description": "Filler",
            "price": 2
        }

        # Add 2 of item to the cart
        cart.add_item(item, restaurant_name, 2)

        # Calculate the total price using the cart_total_price function
        total_price = cart.cart_total_price()

        # Calculate the expected total price based on the added items
        expected_total_price = 2 * 2

        # Check if the calculated total price matches the expected total price
        self.assertEqual(total_price, expected_total_price)

    def test_valid_item_quantity(self):
        # Create a test shopping cart
        cart = ShoppingCart()

        # Define a valid item quantity
        valid_quantity = 5

        # Check if the item quantity is valid using the function
        is_valid = cart.valid_item_quantity(valid_quantity)

        # Assert that the item quantity is valid
        self.assertTrue(is_valid)

    def test_invalid_item_quantity(self):
        # Create a test shopping cart
        cart = self.cart

        # Define an invalid item quantity (e.g., a negative quantity)
        invalid_quantity = -1

        # Check if the item quantity is invalid using the function
        is_valid = cart.valid_item_quantity(invalid_quantity)

        # Assert that the item quantity is invalid
        self.assertFalse(is_valid)


if __name__ == '__main__':
    unittest.main()