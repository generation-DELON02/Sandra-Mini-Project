Order_list=[]
dicts={"customer_name": "John", 
       "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER", 
       "customer_phone": "0789887334", 
       "courier": 2, 
       "status": "preparing" 
       }
Order_list.append(dicts)
def update_order_status():
    get_order_list()
    user_input = int(input("Which order would you like to update it's status: "))
    selected_order = Order_list[user_input-1]
    if user_input ==0:
        order_menu()
    print('You have selected this order')
    print(selected_order)
    stat = input('What is your new order status?: ')
    selected_order["status"] = stat
    print(Order_list)

update_order_status()