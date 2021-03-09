import csv 
from csv import reader
from csv import DictReader


order_list1 = ["customer_name: " ,"customer_address:  " ,"customer_phone:  " ,"courier:   " ,"status:  " ,"items: "]
courier_company_list = ['UberEats', 'Deliveroo', 'JustEat', 'Foodpanda', 'Foodora', 'Zomato']

Drinks_list = []
def read_drinks():
    with open('Drinks_list.csv', 'r', newline ='') as file: 
        dict_reader = DictReader(file)
        for row in dict_reader:
            Drinks_list.append(row)
Courier_list = []
def read_courier(): 
    with open('courier_list.csv', 'r') as f:
        dict_reader1 = DictReader(f)
        for row in dict_reader1:
            Courier_list.append(row)
            print(row)
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
    print('List of Couriers')
    for count, value in enumerate(Courier_list,1):
        print("{}: {}".format(count, value))   
def get_order_list():
    print('***Order List***')
    for count, value in enumerate(Order_list,1):
        print("{}: {}".format(count, value))
           
    #x=int(input("Enter 1 to go back to Main Menu")) call this in order menu later 
    #order_menu()

def new_product():
    while(True):
        new_drink = input("What is the new drink you would like to add?")
        new_price = input("What is the price of the new drink")
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
    while(True):
        new_driver = input("What is the name of the new courier you would like to add: ")
        print("What is the name of the company that the courier is working for: ")
        new_company_courier = input(' or '.join(courier_company_list))
        new_driver_contact = input("What is the new contact number of the driver: ")
        Courier_list.append({
        'courier_name': new_driver,
        'courier_company':new_company_courier,
        'phone': new_driver_contact 
        })
        print('Your Courier has been added successfully')
        print(Courier_list)
        courier_menu()
        #save_courier()
def new_order():
    while(True):
        name = input("What is the name of the customer name you would like to add: ")
        address = input("Enter customer address: ")
        phone = input("Enter customer phone number: ")
        print("which of these couriers is the customer using?")
        courier = input(' or '.join(courier_company_list))
        status = input('press enter to set to status to Preparing:' or 'Preparing')
        Order_list.append({
        "customer_name": name, 
        "customer_address": address, 
        "customer_phone": phone, 
        "courier": courier,
        "status": "Preparing"
        })
        print(Order_list)
        #save_orders()
        cont =input("Want to add another?(Y/N)")
        if cont.upper() == "N":
            order_menu()
            break 
        elif cont.upper()=="Y":
            continue
        else:
            print('Sorry! Input invalid') 
            order_menu()
            break 

def remove_a_product():
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
        remove_a_product()
def remove_a_courier():
    insert=int(input('Press 1 to select the courier you would like to remove or press 0 to cancel'))
    if insert==1:
        get_courier_list()
        courier= int(input('Please confirm the courier you would like to remove: '))-1
        del Courier_list[courier]
        print('Your product has been removed')
        print(Courier_list)
    elif insert==0:
        courier_menu()

def update_order_status():
    print(Order_list)
    user_input3 = int(input("Which order would you like to update it's status or press '0' to cancel: "))
    selected_order = Order_list[user_input3-1]
    if user_input3 == 0:
        order_menu()
    print('You have selected this order')
    print(selected_order)
    stat = input('What is your new order status?: ')
    selected_order["status"] = stat
    print(Order_list)
def update_an_order():
    get_order_list()
    user_input = int(input("Which order would you like to update or press '0' to cancel:"))
    selected_order = Order_list[user_input-1]
    if user_input==0:
        order_menu()
    print('You have selected this order')
    print(selected_order)
    print('Please choose from the options above which part of the Order you would like to update:')
    print('\n'.join(order_list1))
    label = input()
    if label == 'customer_name':
        title = input('Please enter new customer name:')
        selected_order['customer_name'] = title
        print(Order_list)
    elif label == 'customer_address':
        add = input("Please enter new customer address or press 'X' to cancel:")
        selected_order['customer_address'] = add
        print(Order_list)
    elif label == 'customer_phone':
        phone1 = input('Please enter new customer phone number:')
        selected_order['customer_phone'] = phone1
        print(Order_list)
    elif label == 'courier':
        courier1 = input('Please enter new courier:')
        selected_order['courier'] = courier1
        print(Order_list)
    elif label == 'items':
        drink = int(input('What is the item number you would like to add'))
        
        index = Drinks_list.index(drink)
        print(index)
        cont = input("Would you like to add another item? (Y/N)")
        if cont.upper()=="N":
            order_menu()
           
        elif cont.upper() == "Y":
            pass
        else: 
            print('Sorry! Input Invalid')
            order_menu()
        
def update_a_product():
    think=int(input('Press 1 to select the product you would like to update or press 0 to cancel: '))
    if think==1:
        change = input('Which drink would you like to change?: ')
        if change in Drinks_list:
            new=Drinks_list.index(change)
            Drinks_list.remove(change)
            correction = input('Please enter new drink name: ')
            Drinks_list.insert(new,correction)
        else:
            print("Sorry love! Looks like we don't sell that drink!")
    elif think==0:
        drinks_menu()
def update_a_courier():
    print('Please enter the courier you would like to change: ')
    Courier_list.remove(input())
    print('Your product has been removed!')
    print('Please enter the new courier you would like add: ')
    Courier_list.append(input())
    print('Your new courier has been added')
    print(Courier_list)
    courier_menu()

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
        update_order_status()
    if order_input == 4:
        update_an_order()
def order_menu():
    print('***Welcome to the Order Menu***')
    print("Please press '0' to go back to Booze Cafe Menu \nPlease press '1' to print the Order List \nPlease press '2' to create a new order \nPlease press '3' to update Order Status \n Please press '4' to update an Order" )
    data_input = int(input())
    if data_input in (0,1,2,3,4):
        user_input_3(data_input)
    else: 
        print('Sorry! Number is not defined')

def user_input_2(sandy_input):
    if sandy_input == 0:
        print("Welcome to the Cafe's Menu")
        first_menu()
    elif sandy_input == 1:
        get_courier_list()
        x=int(input("Enter 1 to go back to Main Menu"))
        courier_menu()
    elif sandy_input == 2:
        new_courier()
    elif sandy_input ==3:
        update_a_courier()
    elif sandy_input ==4:
        remove_a_courier()
    user_input_2(sandy_input)
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
    elif sandra_input == 3:
        new_product()
    elif sandra_input == 4:
        update_a_product()
    elif sandra_input == 5:
        remove_a_product()
def drinks_menu():
    print("\nPlease click '0' to go back to the main menu\nPlease click '1' to see Cafe Menu \nPlease click '3' to add a new product\nPlease click '4' to update a product\nPlease click '5' to remove a product")
    data_input = int(input())
    if data_input in (0,1,2,3,4,5):
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
        fieldnames = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status']
        writer = csv.DictWriter(g, fieldnames = fieldnames)
        writer.writeheader()
        for line in Order_list:
            writer.writerow(line)
def save_courier():
    with open('courier_list.csv', 'w') as h:
        fieldnames = ['courier_name','courier_company', 'phone']
        writer = csv.DictWriter(h, fieldnames = fieldnames)
        writer.writeheader()
        for line in Courier_list:
            writer.writerow(line)

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