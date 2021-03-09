import pymysql
import os
from dotenv import load_dotenv
import db 


order_list1 = ["customer_name: " ,"customer_address:  " ,"customer_phone:  " ,"courier:   " ,"status:  " ,"items: "]
courier_company_list = ['UberEats', 'Deliveroo', 'JustEat', 'Foodpanda', 'Foodora', 'Zomato']
order_status_list = ["Order recieved", "Order is being prepared", "On its way!",  ]

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

def get_drinks_list():
    def colour_font():
        class color:
            PURPLE = '\033[95m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'
            END = '\033[0m' 
        print(color.PURPLE + color.UNDERLINE + color.BOLD +'***List of Drinks***' + color.END)
    colour_font()
    cursor.execute('SELECT drink_id, drink_name,drink_price FROM drinks_table')
    rows = cursor.fetchall()
    for row in rows: 
        print(f'drink_id: {(row[0])}, drink_name: {row[1]}, drink_price: {row[2]}')
    connection.commit()
def get_courier_list():
    def colour_font():
        class color:
            PURPLE = '\033[95m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'
            END = '\033[0m' 
        print(color.PURPLE + color.UNDERLINE + color.BOLD +'***List of Couriers***' + color.END)
    colour_font()
    cursor.execute('SELECT Courier_id, Courier_name, Courier_company, phone FROM Courier_table') ## does this run if yes connected 
    rows = cursor.fetchall()
    for row in rows:
        print(f'Courier_id:{(row[0])}, Courier_name: {row[1]}, Courier_company: {row[2]}, phone: {row[3]}')
    connection.commit()
def get_order_list():
    def colour_font():
        class color:
            PURPLE = '\033[95m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'
            END = '\033[0m' 
        print(color.PURPLE + color.UNDERLINE + color.BOLD +'***List of Orders***' + color.END)
    colour_font()
    cursor.execute('SELECT customer_id, customer_name, customer_address, customer_phone, courier, status, items FROM order_table')
    rows = cursor.fetchall()
    for row in rows:
        print(f'customer_id: {row[0]}, customer_name: {row[1]}, customer_address: {row[2]}, customer_phone: {row[3]}, courier: {row[4]}, status: {row[5]}, items: {row[6]}')
    connection.commit()

def new_drink():
    while(True):
        new_drink_name = input("What is the new drink you would like to add?")
        new_drink_price = input("What is the price of the new drink?")
        sql = "INSERT INTO drinks_table (drink_name, drink_price) VALUES (%s,%s)"
        val = (new_drink_name, new_drink_price)
        cursor.execute(sql,val)
        connection.commit()
        print('Your new drink has been added!')
        get_drinks_list()
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
        new_courier_name = input("What is the name of the new courier you would like to add: ")
        print('What is the name of the courier company you would like to add')
        new_courier_company = input(' or '.join(courier_company_list))
        new_courier_phone = input('What is the phone number of the new courier:')
        sql = "INSERT INTO Courier_table (Courier_name, Courier_company, phone) VALUES (%s,%s,%s)"
        val = (new_courier_name, new_courier_company, new_courier_phone)
        cursor.execute(sql,val)
        connection.commit()
        print('Your new courier has been added!')
        cont =input("Want to add another?(Y/N)")
        if cont.upper() =="N":
            courier_menu()
            break
        elif cont.upper()== "Y":
            continue
        else:
            print('Sorry! Input invalid')
            courier_menu()
            break    
def new_order():
    while(True):
        new_order_name = input("What is the name of the customer name you would like to add: ")
        new_order_address = input("Enter customer address: ")
        new_order_phone = input("Enter customer phone number: ")
        get_courier_list()
        new_order_courier = input("which of these couriers is the customer using?")
        new_order_status = input('press enter to set to status to Preparing:')
        new_order_drinks = new_drink_to_order()
        new_order_drinks_string = ", ".join(new_order_drinks)
        sql = "INSERT INTO order_table(customer_name, customer_address, customer_phone, courier, status, items) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (new_order_name, new_order_address, new_order_phone, new_order_courier, new_order_status, f'[{new_order_drinks_string}]')
        cursor.execute(sql,val)
        connection.commit()
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
def new_drink_to_order():
    get_drinks_list()
    drinks_list=[]
    print("What is the ID of the drink you would like to add? ")
    while True: #will execute the below statement as long as the condition is true
        try:  #try out some code for testing
            user_input_drink_id = input()
            #to check the product ID exist in the database
            if user_input_drink_id == '0': 
                break      #will break only if 0 is entered and will continue order function 
            chosen_drink = db.get_drink_by_id(user_input_drink_id)
            if chosen_drink ==None:
                print('Sorry wrong number')
                continue #does the while loop again
            drinks_list.append(user_input_drink_id)
        except ValueError:  #not value error another one here name error?
            print('Sorry wrong number!Try again',user_input_drink_id)
            continue #does the while loop again
    return drinks_list


def remove_a_drink():
    remove_a_drink_selection=int(input('Press 1 to confirm the drink you would like to remove \nPress 0 to cancel'))
    if remove_a_drink_selection==1:
        get_drinks_list()
        drink_to_be_removed= int(input('Please confirm the ID of the drink you would like to remove: '))
        sql = "DELETE from drinks_table where drink_id = %s" 
        cursor.execute(sql,drink_to_be_removed) 
        connection.commit()
        print('Your drink has been removed!Please see below')
        get_drinks_list()
        drinks_menu()
    elif remove_a_drink_selection==0:
        drinks_menu()
    else:
        print("I don't know why you pressed that number... so here is the drinks menu again!")
        drinks_menu()
def remove_a_courier():
    remove_courier_selection=int(input('Press 1 to select the courier you would like to remove or press 0 to cancel'))
    if remove_courier_selection==1:
        get_courier_list()
        courier_to_be_removed= int(input('Please confirm the number of courier you would like to remove: '))
        sql = "DELETE from Courier_table where Courier_id = %s"
        cursor.execute(sql,courier_to_be_removed)
        connection.commit()
        print('Your product has been removed please see below')
        get_courier_list()
    elif insert == 0:
        courier_menu()
    else:
        print("I don't know why you pressed that number... so here is the Couriers Menu again!")
        courier_menu()
def remove_an_order():
    remove_an_order_selection = int(input('Press 1 to select the order you would like to remove or press 0 to cancel')) 
    if remove_an_order_selection == 1:
        get_order_list()
        order_to_be_removed = int(input('Please confirm the number of the order you would like to remove or press 0 to cancel:'))
        sql = "DELETE from order_table where customer_id = %s"
        cursor.execute(sql,order_to_be_removed)
        connection.commit()
        print('Your order has been removed please see below')
        get_order_list()
    elif remove_an_order_selection == 0:
        order_menu()
    else: 
        def colour_font():
            class color:
                RED = '\033[91m'
                BOLD = '\033[1m'
                UNDERLINE = '\033[4m'
                END = '\033[0m'
        print(color.RED + color.BOLD + "I don't know why you pressed that number" + color.END)
        colour_font()

def order_selection():
    get_order_list()
    order_to_be_updated = int(input("Which order would you like to update or press '0' to cancel: "))
    database_order_update = "SELECT * FROM order_table Where customer_id = %s"
    cursor.execute(database_order_update, order_to_be_updated)
    selected_order = cursor.fetchone()
    print('You have selected the Order below')
    print(selected_order)
    connection.commit
    if order_to_be_updated == 0:
        order_menu()
    else:
        update_an_order(order_to_be_updated)        
def update_order_status(order_to_be_updated):
    order_selection()
    def colour_font():
        class color:
            PURPLE = '\033[95m'
            BOLD = '\033[1m'
            END = '\033[0m'
    print(color.PURPLE+ color.BOLD + 'What is your new order status?' + color.END)
    colour_font()
    input_updated_order_status = input('\n'.join(order_status_list))
    sql = "UPDATE order_table SET status = %s Where customer_id = %s"
    cursor.execute(sql,(input_updated_order_status, order_to_be_updated)) 
    connection.commit()
    selected_order_status = cursor.fetchone()
    print(selected_courier_name)   
def update_customer_name(order_to_be_updated):
    user_input_customer_name = input("\nPlease enter the updated customer name or press enter to continue\n: ")
    if user_input_customer_name =="":
        def colour_font():
            class color:
                CYAN = '\033[96m'
                BOLD = '\033[1m'
                END = '\033[0m'
            print(color.CYAN + color.BOLD + 'You pressed enter,so no update will be made' + color.END)
        colour_font()
    else:
        sql = "UPDATE order_table SET customer_name = %s Where customer_id = %s"
        cursor.execute(sql,(user_input_customer_name,order_to_be_updated))
        connection.commit()
        selected_customer_name = cursor.fetchone()
        print(selected_customer_name)
def update_customer_address(order_to_be_updated):
    user_input_address = input("\nPlease enter the updated customer address or press enter to continue\n: ")
    if user_input_address == "":
        def colour_font():
            class color:
                CYAN = '\033[96m'
                BOLD = '\033[1m'
                END = '\033[0m'
            print(color.CYAN + color.BOLD + 'You pressed enter,so no update will be made' + color.END)
        colour_font()
    else:
        sql = "UPDATE order_table SET customer_address = %s Where customer_id = %s"
        cursor.execute(sql,(user_input_address,order_to_be_updated))
        connection.commit()
        selected_customer_address = cursor.fetchone()
        #print(selected_customer_address) 
def update_customer_phone(order_to_be_updated):
    user_input_phone = input("\nPlease enter the updated customer phone number or press enter to continue\n: ")
    if user_input_phone == "":
        def colour_font():
            class color:
                CYAN = '\033[96m'
                BOLD = '\033[1m'
                END = '\033[0m'
            print(color.CYAN + color.BOLD + 'You pressed enter,so no update made' + color.END)
        colour_font()
    else:
        sql = "UPDATE order_table SET customer_phone = %s Where customer_id = %s"
        cursor.execute(sql,(user_input_phone, order_to_be_updated))
        connection.commit()
        selected_customer_phone = cursor.fetchone()
        #print(selected_customer_phone)         
def update_customer_courier(order_to_be_updated):
    try:
        get_courier_list()
        user_input_courier = int(input("Please choose the updated courier number that the customer is now using or press enter to continue\n: "))
        if user_input_courier == "":
            def colour_font():
                class color:
                    CYAN = '\033[96m'
                    BOLD = '\033[1m'
                    END = '\033[0m'
                print(color.CYAN + color.BOLD + 'You pressed enter,so no update made' + color.END)
            colour_font()
        else: 
            sql = 'UPDATE order_table SET courier = %s Where customer_id = %s'
            cursor.execute(sql,(user_input_courier))
            selected_customer_courier = cursor.fetchone()
            connection.commit()
            print(selected_customer_courier)
    except: 
        selected_courier_name = cursor.fetchone()
def update_customer_status(order_to_be_updated):
    def colour_font():
        class color:
            CYAN = '\033[96m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'
            END = '\033[0m' 
        print(color.CYAN + color.UNDERLINE + color.BOLD +"What is the new status you would like to update this order with?" + color.END)
    colour_font()
    user_input_status = input(' - '.join(order_status_list))
    if user_input_status == "":
        def colour_font():
            class color:
                CYAN = '\033[96m'
                BOLD = '\033[1m'
                END = '\033[0m'
            print(color.CYAN + color.BOLD + 'You pressed enter,so no update made' + color.END)
        colour_font()
    else: 
        sql = "UPDATE order_table SET status= %s Where customer_id = %s"
        cursor.execute(sql,(user_input_status,order_to_be_updated))
        selected_customer_status = cursor.fetchone()
        connection.commit()
        print(selected_customer_status)
def update_customer_items(order_to_be_updated):
    user_input_drinks = update_drink_in_update_customer()
    user_input_drinks_string = ",".join(user_input_drinks)
    if user_input_drinks == "":
        def colour_font():
            class color:
                CYAN = '\033[96m'
                BOLD = '\033[1m'
                END = '\033[0m'
            print(color.CYAN + color.BOLD + 'You pressed enter,so no update made' + color.END)
        colour_font()
    else: 
        sql = "UPDATE order_table SET items = %s Where customer_id = %s"
        cursor.execute(sql,(f'[{user_input_drinks}]',order_to_be_updated))
        selected_customer_items = cursor.fetchone()
        connection.commit()
def update_drink_in_update_customer():   
    get_drinks_list()
    drinks_list = []
    print('what are the updated IDs of the drinks you would like to add? press 0 once done')
    while True: 
        try:
            user_input_drink_id = input()
            if user_input_drink_id == '0':
                break
            chosen_drink = db.get_drink_by_id(user_input_drink_id)
            if chosen_drink == None:
                print('Sorry wrong number')
                continue
            drinks_list.append(user_input_drink_id)
        except ValueError:
            print('Sorry wrong Number')
            continue
    return drinks_list
def where_to_go_after_update():
    def colour_font():
        class color:
            PURPLE = '\033[95m'
            BOLD = '\033[1m'
            END = '\033[0m'
        print(color.PURPLE+ color.BOLD + 'Your Order has been updated!' + color.END)
    colour_font()
    get_order_list()
    order_menu()
def update_an_order(order_to_be_updated):
    updated_name = update_customer_name(order_to_be_updated)
    updated_address = update_customer_address(order_to_be_updated)
    updated_phone = update_customer_phone(order_to_be_updated)
    updated_courier = update_customer_courier(order_to_be_updated)
    updated_status = update_customer_status(order_to_be_updated)
    updated_item = update_customer_items(order_to_be_updated)
    where_to_go_after_update()

def drinks_selection():
    get_drinks_list()
    drink_to_be_updated = int(input("Please enter the number of the drink you would to update or press 0 to cancel"))
    database_courier_update = "SELECT * FROM drinks_table where drink_id = %s"
    cursor.execute(database_courier_update, drink_to_be_updated)
    selected_drink = cursor.fetchone()
    def colour_font():
        class color:
            PURPLE = '\033[95m'
            BOLD = '\033[1m'
            END = '\033[0m'
        print(color.PURPLE + color.BOLD + 'You have selected the Drink below' + color.END)
    colour_font()
    print(selected_drink)
    if drink_to_be_updated == 0:
        drinks_menu()
    else:
        update_a_drink(drink_to_be_updated)
def update_drink_name(drink_to_be_updated):
    user_input_drink_name = input("\nPlease enter the updated drink name or press enter to continue\n: ")
    if user_input_drink_name == "":
        print("You pressed enter")
    else:
        sql ="UPDATE drinks_table SET drink_name = %s Where drink_id = %s"
        cursor.execute(sql,(user_input_drink_name,drink_to_be_updated))
def update_drink_price(drink_to_be_updated):
    user_input_drink_price = input("\nPlease enter the new price of your updated drink or press enter to continue\n: ")
    if user_input_drink_price == "":
        print("You pressed enter")
    else: 
        sql = "UPDATE drinks_table SET drink_price = %s Where drink_id = %s"
        cursor.execute(sql,(user_input_drink_price,drink_to_be_updated))
        selected_drink_price = cursor.fetchone()
        print(selected_drink_price)
def where_to_go_after_drink_update():
    print('Your drink has been updated')
    get_drinks_list()
    drinks_menu()   
def update_a_drink(drink_to_be_updated):
    updated_drink_name = update_drink_name(drink_to_be_updated)
    updated_drink_price = update_drink_price(drink_to_be_updated)
    where_to_go_after_drink_update()

def courier_selection():
    get_courier_list()
    courier_to_be_updated = int(input("Please confirm which courier you would like to update by entering the ID or press '0' to cancel : "))
    database_courier_update = "SELECT * FROM Courier_table Where Courier_id = %s"
    cursor.execute(database_courier_update, courier_to_be_updated)
    selected_courier = cursor.fetchone()
    print('You have selected the Courier below')
    print(selected_courier)
    connection.commit()
    if courier_to_be_updated == 0:
        courier_menu()
    else:
        update_a_courier(courier_to_be_updated) 
def update_courier_name(courier_to_be_updated):
    user_input_courier_name = input("\nPlease enter the updated courier name or press enter to continue: ")
    if user_input_courier_name =="":
        print("You pressed enter")
    else:
        sql = "UPDATE Courier_table SET Courier_name = %s Where Courier_id = %s"
        cursor.execute(sql,(user_input_courier_name,courier_to_be_updated))
        selected_courier_name = cursor.fetchone()
        print(selected_courier_name)
def update_courier_company(courier_to_be_updated):
    #courier_selection()
    user_input_courier_company = input("\nPlease enter the updated courier company or press enter to continue\n: ")
    if user_input_courier_company =="":
        print("You pressed enter")
    else:
        sql = "UPDATE Courier_table SET Courier_company = %s Where Courier_id = %s"
        cursor.execute(sql,(user_input_courier_company,courier_to_be_updated))
        selected_courier_company = cursor.fetchone()
        print(selected_courier_company)
def update_courier_phone(courier_to_be_updated):
    user_input_courier_phone = input("\nPlease enter the updated courier phone or press enter to continue \n: ")
    if user_input_courier_phone =="":
        print("You pressed enter")
    else:
        sql = "UPDATE Courier_table SET phone = %s Where Courier_id = %s"
        cursor.execute(sql,(user_input_courier_phone, courier_to_be_updated))
        selected_courier_phone = cursor.fetchone()
        print(selected_courier_phone)
def where_to_go_after_courier_update():
    print('Your courier has been updated')
    get_courier_list()
    courier_menu()
    
def update_a_courier(courier_to_be_updated):
    updated_courier_name = update_courier_name(courier_to_be_updated)
    updated_courier_company = update_courier_company(courier_to_be_updated)
    updated_courier_phone = update_courier_phone(courier_to_be_updated)
    where_to_go_after_courier_update()

def user_input_3(order_input): 
    if order_input == 0:
       first_menu()
    if order_input == 1:
        get_order_list()
        x=int(input("Enter 1 to go back to Main Menu"))
        order_menu()
    if order_input == 2:
        new_order()
    if order_input == 3:
        order_selection()
        update_order_status(order_to_be_updated)
    if order_input == 4:
        order_selection()
        update_an_order(order_to_be_updated)
    if order_input == 5:
        remove_an_order()
def order_menu():
    def colour_font():
            class color:
                CYAN = '\033[96m'
                BOLD = '\033[1m'
                UNDERLINE = '\033[4m'
                END = '\033[0m' 
            print(color.CYAN + color.UNDERLINE + color.BOLD +"***Welcome to the Order Menu***" + color.END)
    colour_font()
    print("Please press '0' to go back to Booze Cafe Menu \nPlease press '1' to print the Order List \nPlease press '2' to create a new order \nPlease press '3' to update Order Status \nPlease press '4' to update an order \nPlease press '5' to delete and order")
    data_input = int(input())
    if data_input in (0,1,2,3,4,5):
        user_input_3(data_input)
    else: 
        print('Sorry! Number is not defined')

def user_input_2(courier_input):
    if courier_input == 0:
        def colour_font():
            class color:
                PURPLE = '\033[95m'
                BOLD = '\033[1m'
                UNDERLINE = '\033[4m'
                END = '\033[0m' 
            print(color.PURPLE + color.UNDERLINE + color.BOLD +"***Welcome to the Booze Cafe***" + color.END)
        colour_font()
        first_menu()
    elif courier_input == 1:
        get_courier_list()
        x=int(input("Enter 1 to go back to Main Menu"))
        courier_menu()
    elif courier_input == 2:
        new_courier()
    elif courier_input ==3:
        courier_selection()
        courier_to_be_updated = int(input("Please confirm which courier you would like to update by entering the ID: "))
        selected_courier = cursor.fetchone()
        update_a_courier(courier_to_be_updated)
    elif courier_input ==4:
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
        def colour_font():
            class color:
                PURPLE = '\033[95m'
                BOLD = '\033[1m'
                UNDERLINE = '\033[4m'
                END = '\033[0m' 
            print(color.PURPLE + color.UNDERLINE + color.BOLD +"***Welcome to the Booze Cafe***" + color.END)
        colour_font()
        first_menu()
    elif sandra_input == 1:
        get_drinks_list()
        x=int(input('Enter 1 to go back to Main Menu'))
        drinks_menu()
    elif sandra_input == 2:
        new_drink()
    elif sandra_input == 3:
        drinks_selection()
        update_a_drink(drink_to_be_updated)
    elif sandra_input == 4:
        remove_a_drink()
def drinks_menu():
    print("\nPlease click '0' to go back to the main menu\nPlease click '1' to see Cafe Menu \nPlease click '2' to add a new product\nPlease click '3' to update a drink\nPlease click '4' to remove a drink")
    data_input = int(input())
    if data_input in (0,1,2,3,4):
      user_input_1(data_input) 
    else:
        print('Number is not defined')

def first_menu():
    def colour_font():
            class color:
                PURPLE = '\033[95m'
                BOLD = '\033[1m'
                UNDERLINE = '\033[4m'
                END = '\033[0m' 
            print(color.PURPLE + color.UNDERLINE + color.BOLD +"***Welcome to the Booze Cafe***" + color.END)
    colour_font()
    data_input = int(input("Please press 0 to exit the app \nPlease press 1 to see the Drinks Menu \nPlease press 2 to see the Courier Menu \nPlease press 3 to see the Order Menu"))
    if data_input == 3:
        order_menu()
    elif data_input ==2:
        def colour_font():
            class color:
                CYAN = '\033[96m'
                BOLD = '\033[1m'
                UNDERLINE = '\033[4m'
                END = '\033[0m' 
            print(color.CYAN + color.UNDERLINE + color.BOLD +"***Welcome to the Courier Menu***" + color.END)
        colour_font()
        courier_menu()
    elif data_input ==1:
        def colour_font():
            class color:
                CYAN = '\033[96m'
                BOLD = '\033[1m'
                UNDERLINE = '\033[4m'
                END = '\033[0m' 
        print(color.CYAN + color.UNDERLINE + color.BOLD +"***Welcome to the Drinks(product) Menu***" + color.END)
        colour_font()
        drinks_menu()
    elif data_input ==0:
        def colour_font():
            class color:
                PURPLE = '\033[95m'
                BOLD = '\033[1m'
                UNDERLINE = '\033[4m'
                END = '\033[0m' 
            exit(color.PURPLE + color.UNDERLINE + color.BOLD +"***Bye, Hope to see you soon! ***" + color.END)
        colour_font()

def main():
    first_menu()

if __name__=='__main__':
    main()


