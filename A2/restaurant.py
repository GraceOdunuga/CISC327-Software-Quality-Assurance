import csv
from menu import Item, RestaurantMenu

restaurant_file = 'restaurant2.csv'



class Restaurant:
    def __init__(self, id_num, name, address, category, price_range, open_time, close_time):
        self.id_num = id_num
        self.name = name
        self.address = address
        self.category = category
        self.price_range = price_range
        self.open_time = open_time
        self.close_time = close_time
        self.menu = None
        self.get_menu()
    # Create and set the menu for the restaurant
    def get_menu(self):
        menu = RestaurantMenu(self.id_num)
        self.menu = menu

    def show_menu(self):
        if self.menu:
            print(f"Menu for {self.name}:")
            self.menu.show_menu()
        else:
            print(f"No menu available for {self.name}")


restaurants_all = []
with open(restaurant_file, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) 
    for row in reader:
        restaurant = Restaurant(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        restaurants_all.append(restaurant)
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
