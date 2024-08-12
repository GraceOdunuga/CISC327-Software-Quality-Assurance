import pymongo
import csv
from restaurant_init_helper import Restaurant

# When running this file, accesses all restaurants and their menus, and allows
# adding them to DB table, viewing the DB table, or dropping the table.
restaurant_file = "C:/Users/trayb/Documents/School Files/University/Courses/Fall23/CISC327/CISC327-group24-project/A3/src/db_setup/restaurant.csv"

restaurants_all = []
with open(restaurant_file, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) 
    for row in reader:
        # order of rows:
        # id 0, name 1, category 2, price_range 3, address 4, open_time 5, close_time 6

        # order of restaurant in table:
        # id, name, address, category, price_range, open_time, close_time
        restaurant = Restaurant(row[0], row[1], row[4], row[2], row[3], row[5], row[6])
        restaurants_all.append(restaurant)

def main():
    # Access MongoDB database
    mongo_url = 'mongodb+srv://group24:eyljlgY1EkNeE8AB@group24-project.rv8qyhx.mongodb.net/?retryWrites=true&w=majority'
    client = pymongo.MongoClient(mongo_url)
    db = client['backend-database'] # database
    restaurants_table = db['restaurants'] # restaurants table

    while(True):
        print("0: Exit")
        print("1: Add all restaurants to DB")
        print("2: View all restaurants in DB")
        print("3: Drop restaurant table")
        choice = (int)(input("Enter choice: "))
        if choice == 0:
            break
        elif choice == 1:
            restaurants = list(restaurants_table.find())
            if restaurants:
                print("All restaurants already in DB.\n")
            else:
                for r in restaurants_all:
                    restaurant_data = {
                        "id_num": r.id_num,
                        "name": r.name,
                        "address": r.address,
                        "category": r.category,
                        "price_range": r.price_range,
                        "open_time": r.open_time,
                        "close_time": r.close_time,
                        "menu": r.menu
                    }
                    restaurants_table.insert_one(restaurant_data)
                print("Restaurants added.\n")
        elif choice == 2:
            restaurants = list(restaurants_table.find())
            if len(restaurants) == 0:
                print("Table empty. Add restaurants.\n")
            else:
                for r in restaurants:
                    print(r)
        elif choice == 3:
            restaurants_table.drop()
            print("Table dropped.")
        else:
            print("Invalid input. Please try again.\n")

if __name__ == '__main__':
    main()