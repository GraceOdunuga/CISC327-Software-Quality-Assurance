import csv

# Define the CSV files containing menus for initialization
menu_file = "C:/Users/trayb/Documents/School Files/University/Courses/Fall23/CISC327/CISC327-group24-project/A3/src/db_setup/restaurant-menus.csv" # change to absolute path to this directory to work

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