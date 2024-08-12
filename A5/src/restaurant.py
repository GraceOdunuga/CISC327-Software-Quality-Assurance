import csv

# Define the CSV files containing menus for initialization
menu_file = "C:/Users/trayb/Documents/School Files/University/Courses/Fall23/CISC327/CISC327-group24-project/A3/src/db_setup/restaurant-menus.csv" # change to absolute path to this directory to work

# For creating and storing information about a restaruant, including: id, name, address, category, price range, opening time, closing time, and menu
# Contains methods for initializing & viewing menu
class Restaurant:
    def __init__(self, id_num, name, address, category, price_range, open_time, close_time, menu=None):
        self.id_num = id_num
        self.name = name
        self.address = address
        self.category = category
        self.price_range = price_range
        self.open_time = open_time
        self.close_time = close_time
        self.menu = menu
        self.get_menu()

    # Create and set the menu for the restaurant
    def get_menu(self):
        menu = {} # dict containing dicts
        # e.g. {item_name: {category: ..., description: ..., price: ...}}
        with open(menu_file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                #print(row[1], self.name)
                if row[0] == self.id_num:
                    # Extract and parse the item price
                    price_str = row[4].replace(' USD', '')  # Remove "USD" and any leading/trailing spaces
                    price = float(price_str)
                    menu[row[2]] = {
                        "name": row[2],
                        "category": row[1],
                        "description": row[3],
                        "price": price
                    }
        self.menu = menu

    # Method to show restaurant menus
    def show_menu(self):
        string = ""
        if self.menu:
            items = self.menu.keys()

            categories_list = set()
            for item in items:
                categories_list.add(self.menu[item]['category'])

            for category in categories_list:
                print(f"Category: {category}") 
                for item in items:
                    if self.menu[item]['category'] == category:
                        print(f"{item} - {self.menu[item]['description']} - ${self.menu[item]['price']}\n")
                        string += f"{item} - {self.menu[item]['description']} - ${self.menu[item]['price']}\n"
                print("")
        else:
            print(f"No menu available for {self.name}")
        return string

# Example usage:
# if __name__ == "__main__":
#     restaurant_id = '1'
#     restaurant_name = 'Sample Restaurant'
#     restaurant_address = '123 Main Street'
#     restaurant_category = 'Italian'
#     restaurant_price_range = '$$'
#     restaurant_open_time = '10:00 AM'
#     restaurant_close_time = '9:00 PM'

#     restaurant = Restaurant(restaurant_id, restaurant_name, restaurant_address, restaurant_category, restaurant_price_range, restaurant_open_time, restaurant_close_time)

#     # Show the restaurant's menu
#     restaurant.show_menu()
