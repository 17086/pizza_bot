#list to store ordered pizzas
order_list =[]
#list to store pizza's prices 
order_cost =[]

#Customer details dictionary
customer_details = {}


print ("Do you want to start another Order or exit?")
print ("To start another order enter 1.")
print ("To exit the Bot enter 2.")


while True:
    try:
        confirm = int(input ("Please enter a number "))
        if confirm >= 1 and confirm <= 2:
         if confirm == 1:
            print ("New Order")
            order_list.clear()
            order_cost.clear()
            customer_details.clear()
            break

         elif  confirm == 2:
             print ("Exit")
             order_list.clear()
             order_cost.clear()
             customer_details.clear()
             main()
             break
        else: 
            print ("Number must be 1 or 2")
    except ValueError:
        print ("That is not a valid number.")
        print ("Please enter 1 or 2.")
    
def main():
    print("Start again")
