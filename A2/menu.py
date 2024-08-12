import csv

# Define the CSV file containing restaurant menus
menu_file = 'restaurant-menus2.csv'

# Class to represent an individual menu item
class Item:
    def __init__(self, name, category, description, price):
        self.name = name
        self.category = category
        self.description = description
        self.price = price

# Class to represent a restaurant's menu
class RestaurantMenu:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.items = []
        self.load_menu(menu_file)

    # Method to load the menu from a CSV file
    def load_menu(self, menu_file):
        menus = []
        with open(menu_file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == self.restaurant_name:
                    # Extract and parse the item price
                    price_str = row[4].replace(' USD', '')  # Remove "USD" and any leading/trailing spaces
                    price = float(price_str)
                    item = Item(row[2], row[1], row[3], price)
                    menus.append(item)
        self.items = menus
    
    # Method to display the menu
    def show_menu(self):
        categories_list = set()
        for item in self.items:
            categories_list.add(item.category)

        for category in categories_list:
            print(f"Category: {category}") 
            for item in self.items:
                if item.category == category:
                    print(f"{item.name} - ${item.price}")

# Uncomment the following code if you want to test the menu loading and display functionality
# if __name__ == "__main__":
#     menu_file = 'restaurant-menus2.csv'
#     restaurant_name = '1'
#     restaurant_menu = RestaurantMenu(restaurant_name)
#     print(f"Menu for {restaurant_name}:")
#     restaurant_menu.show_menu()

#     # Test to view an item's price
#     while True:
#         item_name = input("Enter the name of the item to view its price (or type 'exit' to quit): ")
#         if item_name.lower() == 'exit':
#             break

#         found = False
#         for item in restaurant_menu.menu:
#             if item.name == item_name:
#                 print(f"{item.name} - ${item.price}")
#                 found = True
#                 break

#         if not found:
#             print(f"Item '{item_name}' not found in the menu.")
