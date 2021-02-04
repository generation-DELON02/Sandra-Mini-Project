#create a json file with dict info 
#open json file 
#pass dictionary through to json 
#write to json file 
import json


order_list=[]
dicts={ "customer_name": "John", "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER", "customer_phone": "0789887334", "courier": 2, "status": "preparing" }
order_list.append(dicts)
order_list.append(dicts)
print(order_list)

with open('list_of_dicts.json', 'w') as outfile:
   json.dump(order_list, outfile)

with open('list_of_dicts.json', 'r') as outfile:
    data=json.load(outfile)
    print(data)



