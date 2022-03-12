

#list to store ordered pizzas
order_list =['Margherita', 'Hawaiian','Vegan','BBQ Chicken Deluxe']
#list to store pizza's prices 
order_cost =[8.50, 8.50, 8.50, 13.50]

cust_details = {'name': 'Jayden', 'phone': '0213345656', 'house': '45', 'street': 'Harry', 'suburb': 'Howick'}

for item in order_list:
    print( "Ordered: {}  Cost: ${:.2f}" .format(item, order_cost[count]))
    count = count+1

 
