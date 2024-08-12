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

    def test_valid_item_quantity1(self):
            # Create a test shopping cart
            cart = ShoppingCart()

            # Define quantity < 0, which is invalid
            valid_quantity = -1

            # Check if the item quantity is valid using the function
            is_valid = cart.valid_item_quantity(valid_quantity)

            # Assert that the item quantity is invalid
            self.assertFalse(is_valid)

    def test_valid_item_quantity2(self):
            # Create a test shopping cart
            cart = ShoppingCart()

            # Define quantity == 0, which is invalid
            valid_quantity = 0

            # Check if the item quantity is valid using the function
            is_valid = cart.valid_item_quantity(valid_quantity)

            # Assert that the item quantity is invalid
            self.assertFalse(is_valid)

    def test_valid_item_quantity3(self):
            # Create a test shopping cart
            cart = ShoppingCart()

            # Define quantity > 0, which is valid
            valid_quantity = 2

            # Check if the item quantity is valid using the function
            is_valid = cart.valid_item_quantity(valid_quantity)

            # Assert that the item quantity is valid
            self.assertTrue(is_valid)

    def test_modify_profile1(self):
        # Initialize a test user profile
        test_user = UserProfile("Test User", "test@test.com", "1234567890", "Test Address", "password123")
        
        # Define new profile information 
        new_phone_number = "0" # invalid
        new_email = "bob@gmail.com" # valid
        new_address = "New Address"
        old_password = "password123" 
        new_password = "bobisepic123" # valid
        
        # Ensure old password is same as stored one
        self.assertEqual(test_user.password, old_password)

        # Try to modify profile, ensure credential check fails & returns False
        result = test_user.modify_profile(new_email, new_phone_number, new_address, new_password)
        self.assertFalse(result)

        # Check if the profile information is unmodified
        self.assertNotEqual(test_user.phone_number, new_phone_number)
        self.assertNotEqual(test_user.email, new_email)
        self.assertNotEqual(test_user.address, new_address)
        self.assertNotEqual(test_user.password, new_password)

    def test_modify_profile2(self):
        # Initialize a test user profile
        test_user = UserProfile("Test User", "test@test.com", "1234567890", "Test Address", "password123")
        
        # Modify the profile information 
        new_phone_number = "1111111111" # valid
        new_email = "bob" # invalid
        new_address = "New Address"
        old_password = "password123" 
        new_password = "bobisepic123" # valid
        
        # Ensure old password is same as stored one
        self.assertEqual(test_user.password, old_password)

        # Try to modify profile, ensure credential check fails & returns False
        result = test_user.modify_profile(new_email, new_phone_number, new_address, new_password)
        self.assertFalse(result)

        # Check if the profile information is unmodified
        self.assertNotEqual(test_user.phone_number, new_phone_number)
        self.assertNotEqual(test_user.email, new_email)
        self.assertNotEqual(test_user.address, new_address)
        self.assertNotEqual(test_user.password, new_password)

    def test_modify_profile3(self):
        # Initialize a test user profile
        test_user = UserProfile("Test User", "test@test.com", "1234567890", "Test Address", "password123")
        
        # Modify the profile information 
        new_phone_number = "1111111111" # valid
        new_email = "bob@gmail.com" # valid
        new_address = "New Address"
        old_password = "password123" 
        new_password = "bob" # invalid
        
        # Ensure old password is same as stored one
        self.assertEqual(test_user.password, old_password)

        # Try to modify profile, ensure credential check fails & returns False
        result = test_user.modify_profile(new_email, new_phone_number, new_address, new_password)
        self.assertFalse(result)

        # Check if the profile information is unmodified
        self.assertNotEqual(test_user.phone_number, new_phone_number)
        self.assertNotEqual(test_user.email, new_email)
        self.assertNotEqual(test_user.address, new_address)
        self.assertNotEqual(test_user.password, new_password)

    def test_modify_profile4(self):
        # Initialize a test user profile
        test_user = UserProfile("Test User", "test@test.com", "1234567890", "Test Address", "password123")
        
        # Modify the profile information 
        new_phone_number = "0" # invalid
        new_email = "bob" # invalid
        new_address = "New Address"
        old_password = "password123" 
        new_password = "bobisepic123" #valid
        
        # Ensure old password is same as stored one
        self.assertEqual(test_user.password, old_password)

        # Try to modify profile, ensure credential check fails & returns False
        result = test_user.modify_profile(new_email, new_phone_number, new_address, new_password)
        self.assertFalse(result)

        # Check if the profile information is unmodified
        self.assertNotEqual(test_user.phone_number, new_phone_number)
        self.assertNotEqual(test_user.email, new_email)
        self.assertNotEqual(test_user.address, new_address)
        self.assertNotEqual(test_user.password, new_password)

    def test_modify_profile5(self):
        # Initialize a test user profile
        test_user = UserProfile("Test User", "test@test.com", "1234567890", "Test Address", "password123")
        
        # Modify the profile information 
        new_phone_number = "0" # invalid
        new_email = "bob@gmail.com" #valid
        new_address = "New Address"
        old_password = "password123" 
        new_password = "bob" # invalid
        
        # Ensure old password is same as stored one
        self.assertEqual(test_user.password, old_password)

        # Try to modify profile, ensure credential check fails & returns False
        result = test_user.modify_profile(new_email, new_phone_number, new_address, new_password)
        self.assertFalse(result)

        # Check if the profile information is unmodified
        self.assertNotEqual(test_user.phone_number, new_phone_number)
        self.assertNotEqual(test_user.email, new_email)
        self.assertNotEqual(test_user.address, new_address)
        self.assertNotEqual(test_user.password, new_password)

    def test_modify_profile6(self):
        # Initialize a test user profile
        test_user = UserProfile("Test User", "test@test.com", "1234567890", "Test Address", "password123")
        
        # Modify the profile information 
        new_phone_number = "1111111111" # valid
        new_email = "bob" # invalid
        new_address = "New Address"
        old_password = "password123" 
        new_password = "bob" # invalid
        
        # Ensure old password is same as stored one
        self.assertEqual(test_user.password, old_password)

        # Try to modify profile, ensure credential check fails & returns False
        result = test_user.modify_profile(new_email, new_phone_number, new_address, new_password)
        self.assertFalse(result)

        # Check if the profile information is unmodified
        self.assertNotEqual(test_user.phone_number, new_phone_number)
        self.assertNotEqual(test_user.email, new_email)
        self.assertNotEqual(test_user.address, new_address)
        self.assertNotEqual(test_user.password, new_password)

    def test_modify_profile7(self):
        # Initialize a test user profile
        test_user = UserProfile("Test User", "test@test.com", "1234567890", "Test Address", "password123")
        
        # Modify the profile information 
        new_phone_number = "1111111111" # valid
        new_email = "bob@gmail.com" # valid
        new_address = "New Address"
        old_password = "password123" 
        new_password = "bobisepic123" # valid
        
        # Ensure old password is same as stored one
        self.assertEqual(test_user.password, old_password)

        # Try to modify profile, ensure credential check passes & returns True
        result = test_user.modify_profile(new_email, new_phone_number, new_address, new_password)
        self.assertTrue(result)

        # Check if the profile information is modified
        self.assertEqual(test_user.phone_number, new_phone_number)
        self.assertEqual(test_user.email, new_email)
        self.assertEqual(test_user.address, new_address)
        self.assertEqual(test_user.password, new_password)

    def test_modify_profile8(self):
        # Initialize a test user profile
        test_user = UserProfile("Test User", "test@test.com", "1234567890", "Test Address", "password123")
        
        # Modify the profile information 
        new_phone_number = "0" # invalid
        new_email = "bob" # invalid
        new_address = "New Address"
        old_password = "password123" 
        new_password = "bob" # invalid
        
        # Ensure old password is same as stored one
        self.assertEqual(test_user.password, old_password)

        # Try to modify profile, ensure credential check fails & returns False
        result = test_user.modify_profile(new_email, new_phone_number, new_address, new_password)
        self.assertFalse(result)

        # Check if the profile information is unmodified
        self.assertNotEqual(test_user.phone_number, new_phone_number)
        self.assertNotEqual(test_user.email, new_email)
        self.assertNotEqual(test_user.address, new_address)
        self.assertNotEqual(test_user.password, new_password)


if __name__ == '__main__':
    unittest.main()