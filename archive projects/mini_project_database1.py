import csv 
from csv import reader
from csv import DictReader
import pymysql
import os
from dotenv import load_dotenv


#status_list = ['']
order_list1 = ["customer_name: " ,"customer_address:  " ,"customer_phone:  " ,"courier:   " ,"status:  " ,"items: "]
courier_company_list = ['UberEats', 'Deliveroo', 'JustEat', 'Foodpanda', 'Foodora', 'Zomato']

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

connection = pymysql.connect(
    host,
    user,
    password,
    database
)
cursor = connection.cursor()

Drinks_list = []
def read_drinks():
    with open('Drinks_list.csv', 'r', newline ='') as file: 
        dict_reader = DictReader(file)
        for row in dict_reader:
            Drinks_list.append(row)

Order_list = []      
def read_order():
    with open('order_list.csv', 'r') as g:
        dict_reader2 = DictReader(g)
        for row in dict_reader2:
            Order_list.append(row)

def get_drinks_list():
    print('***List of Drinks(Menu)***')
    for count, value in enumerate(Drinks_list,1):
        print("{}: {}".format(count, value))
def get_courier_list():
    print('****List of Couriers****')
    cursor.execute('SELECT Courier_id, Courier_name, Courier_company, phone FROM Courier_table') ## does this run if yes connected 
    rows = cursor.fetchall()
    for row in rows:
        print(f'Courier_id: {(row[0])}, Courier_name: {row[1]}, Courier_company: {row[2]}, phone: {row[3]}')

    cursor.close()
    connection.close()
    #cursor.execute('SELECT Courier_id, Courier_name, Courier_company, phone FROM Courier_table')
    #rows = cursor.fetchall()
    #for row in rows:
    #    print(f'Courier_id: {(row[0])}, Courier_name: {row[1]}, Courier_company: {row[2]}, phone: {row[3]}')
def get_order_list():
    print('***Order List***')
    for count, value in enumerate(Order_list,1):
        print("{}: {}".format(count, value))
           
    #x=int(input("Enter 1 to go back to Main Menu")) call this in order menu later 
    #order_menu()

def new_product():
    while(True):
        new_drink = input("What is the new drink you would like to add?")
        new_price = input("What is the price of the new drink?")
        Drinks_list.append({
            "name":new_drink,
            "price":new_price
        })
        print(Drinks_list)
        #save_drinks()
        cont =input("Want to add another?(Y/N)")
        if cont.upper() =="N":
            drinks_menu()
            break
        elif cont.upper()== "Y":
            continue
        else:
            print('Sorry! Input invalid')
            drinks_menu()
            break
def new_courier():


        # print("What is the name of the company that the courier is working for: ")
        # new_company_courier = input(' or '.join(courier_company_list))
        # new_driver_contact = input("What is the new contact number of the driver: ")
        # Courier_list.append({
        # 'courier_name': new_driver,
        # 'courier_company':new_company_courier,
        # 'phone': new_driver_contact 
        # })
        #print('Your Courier has been added successfully')
        #print(Courier_list)
        #courier_menu()
        #save_courier()
#def new_order():
#   while(True):
#        name = input("What is the name of the customer name you would like to add: ")
#        address = input("Enter customer address: ")
#        phone = input("Enter customer phone number: ")
#        get_courier_list()
#        courier = input("which of these couriers is the customer using?")
#        status = input('press enter to set to status to Preparing:')
#        drinks = new_drink_to_order()
#        Order_list.append({
#        "customer_name": name, 
#        "customer_address": address, 
#         "customer_phone": phone, 
#        "courier": courier,
#        "status": "preparing",
#        "drink_order": drinks
#        })
#        more_drinks = another_drink_to_be_added()
#        print(more_drinks[0])
#        drinks.append(more_drinks[0]) 
#        print(Order_list)
        #save_orders()
        
#        cont =input("Want to add another?(Y/N)")
#        if cont.upper() == "N":
#            order_menu()
#            break 
#        elif cont.upper()=="Y":
#            continue
#        else:
#            print('Sorry! Input invalid') 
#            order_menu()
#            break 
def new_drink_to_order():
    get_drinks_list()
    list_of_drink_index = []
    drinks = list_of_drink_index
    while True:
        try: 
            user_input_drink = int(input("What number drink would you like to add? "))
            Drinks_list[user_input_drink-1]
            drinks.append(user_input_drink) 
            return drinks   
            print(drinks) 
        except ValueError:
            print('Sorry wrong number!Try again')
            continue
        if user_input_drink == 0: 
            ValueError
            continue
    new_drink_to_order()    
    #return list_of_drink_index

def another_drink_to_be_added():
    keep_going = input('Would you like to add another drink')
    if keep_going.upper() == "N":
        order_menu()
        #break
    elif keep_going.upper() =="Y":
        return new_drink_to_order()
        
    else:
        print('Sorry! Invalid Input!')
        order_menu()
        #break

def remove_a_drink():
    insert=int(input('Press 1 to confirm the product you would like to remove \nPress 0 to cancel'))
    if insert==1:
        get_drinks_list()
        drink= int(input('Please confirm the number of the  drink you would like to remove: '))-1
        del Drinks_list[drink]
        save_drinks()
        #Drinks_list.remove(input())  
        print('Your product has been removed')
        print(Drinks_list)
    elif insert==0:
        drinks_menu()
    else:
        print("I don't know why you pressed that number... so here is the drinks menu again!")
        remove_a_product()
def remove_a_courier():
    insert=int(input('Press 1 to select the courier you would like to remove or press 0 to cancel'))
    if insert==1:
        get_courier_list()
        courier= int(input('Please confirm the number of courier you would like to remove: '))-1
        del Courier_list[courier]
        print('Your product has been removed please see below')
        print(Courier_list)
    elif insert == 0:
        courier_menu()
def remove_an_order():
    insert = int(input('Press 1 to select the order you would like to remove or press 0 to cancel')) 
    if insert == 1:
        get_order_list()
        order_to_be_removed = int(input('Please confirm the number of the order you would like to remove or press 0 to cancel:'))-1
        del Order_list[order_to_be_removed]
        print('Your order has been removed please see below')
        print(Order_list)
    elif insert == 0:
        order_menu()

def order_selection():
    get_order_list()
    user_input3 = int(input("Which order would you like to update or press '0' to cancel: "))
    selected_order = Order_list[user_input3-1]
    print('You have selected the order below')
    print(selected_order)
    if user_input3 == 0:
        order_menu()
    else:
        update_an_order(selected_order)
def update_order_status(selected_order):
    order_selection()
    stat = input('What is your new order status?: ')
    selected_order["status"] = stat
    print(Order_list)
def update_customer_name(selected_order):
    user_input_name = input("\nPlease enter the updated customer name or press enter to continue\n: ")
    if user_input_name =="":
        print("You pressed enter")
    else:
        selected_order['customer_name'] = user_input_name
        return user_input_name
def update_customer_address(selected_order):
    user_input_address = input("\nPlease enter the updated customer address or press enter to continue\n: ")
    if user_input_address == "":
        print("You pressed enter")
    else:
        selected_order['customer_address'] = user_input_address
        return user_input_address
def update_customer_phone(selected_order):
    user_input_phone = input("\nPlease enter the updated customer phone number or press enter to continue\n: ")
    if user_input_phone == "":
        print("You pressed enter")
    else: 
        selected_order['customer_phone'] = user_input_phone
        return user_input_phone
def update_customer_courier(selected_order):
    try:
        get_courier_list()
        user_input_courier = int(input("Please choose the updated courier number that the customer is now using or press enter to continue\n: "))
        if user_input_courier == "":
            print("You pressed enter")

        else: 
            selected_order['courier'] = user_input_courier
            return user_input_courier
    except: 
        updated_customer_courier(selected_order)
def update_customer_status(selected_order):
    user_input_status = (input("Please choose what you would like to update the status to: "))
    if user_input_status == "":
        print("You pressend enter")
    else: 
        selected_order['status'] = user_input_status
        return user_input_courier

def where_to_go_after_update():
    get_order_list()
    order_menu()
    print('Your order has been updated')
def update_an_order(selected_order):
    updated_name = update_customer_name(selected_order)
    updated_address = update_customer_address(selected_order)
    updated_phone = update_customer_phone(selected_order)
    updated_courier = update_customer_courier(selected_order)
    updated_status = update_customer_status(selected_order)
    where_to_go_after_update()

def drinks_selection():
    get_drinks_list()
    drink_to_be_updated = int(input("Please enter the number of the drink you would to update or press 0 to cancel"))
    selected_drink = Drinks_list[drink_to_be_updated-1]
    print('You have selected the drink below')
    print(selected_drink)
    if drink_to_be_updated == 0:
        drinks_menu()
    else:
        update_a_drink(selected_drink)
def update_drink_name(selected_drink):
    user_input_drink_name = input("\nPlease enter the updated drink name or press enter to continue\n: ")
    if user_input_drink_name == "":
        print("You pressed enter")
    else:
        selected_drink['name'] = user_input_drink_name
        return user_input_drink_name
def update_drink_price(selected_drink):
    user_input_drink_price = input("\nPlease enter the new price of your updated drink or press enter to continue\n: ")
    if user_input_drink_price == "":
        print("You pressed enter")
    else: 
        selected_drink['price'] = user_input_drink_price
        return user_input_drink_price
def where_to_go_after_drink_update():
    get_drinks_list()
    drinks_menu()
    print('Your drink has been updated')
def update_a_drink(selected_drink):
    updated_drink_name = update_drink_name(selected_drink)
    updated_drink_price = update_drink_price(selected_drink)
    where_to_go_after_drink_update()

def courier_selection():
    get_courier_list()
    courier_to_be_updated = int(input("Please confirm which courier you would like to update by entering the number: "))
    selected_courier = Courier_list[courier_to_be_updated-1]
    print('You have selected the courier below')
    print(selected_courier)
    if courier_to_be_updated ==0:
        courier_menu()
    else:
        update_a_courier(selected_courier)
def update_courier_name(selected_courier):
    user_input_courier_name = input("\nPlease enter the updated courier name or press enter to continue: ")
    if user_input_courier_name =="":
        print("You pressed enter")
    else:
        selected_courier['courier_name'] = user_input_courier_name
        return user_input_courier_name
def update_courier_company(selected_courier):
    user_input_courier_company = input("\nPlease enter the updated courier company or press enter to continue\n: ")
    if user_input_courier_company =="":
        print("You pressed enter")
    else:
        selected_courier['courier_name'] = user_input_courier_company
        return user_input_courier_company
def update_courier_phone(selected_courier):
    user_input_courier_phone = input("\nPlease enter the updated courier phone or press enter to continue \n: ")
    if user_input_courier_phone =="":
        print("You pressed enter")
    else:
        selected_courier['phone'] = user_input_courier_phone
        return user_input_courier_phone
def where_to_go_after_courier_update():
    get_courier_list()
    courier_menu()
    print('Your courier has been updated')
def update_a_courier(selected_courier):
    updated_courier_name = update_courier_name(selected_courier)
    updated_courier_company = update_courier_company(selected_courier)
    updated_courier_price = update_courier_phone(selected_courier)
    where_to_go_after_courier_update()

def user_input_3(order_input):
    if order_input == 0:
        print("***Welcome to the Cafe's Menu***")
        first_menu()
    if order_input == 1:
        get_order_list()
        x=int(input("Enter 1 to go back to Main Menu"))
        order_menu()
    if order_input == 2:
        new_order()
    if order_input == 3:
        order_selection()
        update_order_status(selected_order)
    if order_input == 4:
        order_selection()
        user_input3 = int(input("Which order would you like to update or press '0' to cancel: "))
        selected_order = Order_list[user_input3-1]
        update_an_order(selected_order)
    if order_input == 5:
        remove_an_order()
def order_menu():
    print('***Welcome to the Order Menu***')
    print("Please press '0' to go back to Booze Cafe Menu \nPlease press '1' to print the Order List \nPlease press '2' to create a new order \nPlease press '3' to update Order Status \nPlease press '4' to update an order \nPlease press '5' to delete and order")
    data_input = int(input())
    if data_input in (0,1,2,3,4,5):
        user_input_3(data_input)
    else: 
        print('Sorry! Number is not defined')

def user_input_2(user_courier_input):
    if user_courier_input == 0:
        print("Welcome to the Cafe's Menu")
        first_menu()
    elif user_courier_input == 1:
        get_courier_list()
        x=int(input("Enter 1 to go back to Main Menu"))
        courier_menu()
    elif user_courier_input == 2:
        new_courier()
    elif user_courier_input ==3:
        courier_selection()
        update_a_courier(selected_courier)
    elif user_courier_input ==4:
        remove_a_courier()
    user_input_2(courier_input)
def courier_menu():
    print('***Welcome to the Courier Menu***')
    print("Please click '0' to go back to Booze Cafe Menu \nPlease click '1' to see Courier List \nPlease click '2' to add a new courier \nPlease click '3' to update a courier \nPlease click '4' to remove a courier")
    data_input = int(input())
    if  data_input in (0,1,2,3,4):
        user_input_2(data_input)
    else:
        print('Number is not defined')
    courier_menu()

def user_input_1(sandra_input):
    if sandra_input == 0:
        print("Welcome back to the first menu")
        first_menu()
    elif sandra_input == 1:
        get_drinks_list()
        x=int(input('Enter 1 to go back to Main Menu'))
        drinks_menu()
    elif sandra_input == 2:
        new_product()
    elif sandra_input == 3:
        drinks_selection()
        update_a_drink(selected_drink)
    elif sandra_input == 4:
        remove_a_drink()
def drinks_menu():
    print("\nPlease click '0' to go back to the main menu\nPlease click '1' to see Cafe Menu \nPlease click '2' to add a new product\nPlease click '3' to update a drink\nPlease click '4' to remove a drink")
    data_input = int(input())
    if data_input in (0,1,2,3,4):
      user_input_1(data_input) 
    else:
        print('Number is not defined')

def save_drinks():                #open the file>put list in file>close file 
    with open('Drinks_list.csv','w') as f: 
        fieldnames = ['name', 'price']
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
        for line in Drinks_list:
            writer.writerow(line)
def save_orders():
    with open('order_list.csv','w') as g:
        fieldnames = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status','drink_order']
        writer = csv.DictWriter(g, fieldnames = fieldnames)
        writer.writeheader()
        for line in Order_list:
            writer.writerow(line)
def save_courier():
    cursor.close()
    connection.close()

def first_menu():
    print('***Welcome to Booze Cafe***')
    data_input = int(input("Please click '3' to see Order Menu \nPlease click '2' to see courier menu \nPlease click '1' to see the drinks menu \nPlease click '0' to exit the app"))
    if data_input == 3:
        print("***Welcome to the Order Menu***")
        order_menu()
    elif data_input ==2:
        print("***Welcome to the Couriers Menu***")
        courier_menu()
    elif data_input ==1:
        print("***Welcome to the Cafe's Drinks Menu***")
        drinks_menu()
    elif data_input ==0:
        save_drinks()
        save_courier()
        save_orders()
        exit("See you Later")

def main():
    read_courier()
    read_drinks()
    read_order()
    first_menu()

if __name__=='__main__':
    main()

