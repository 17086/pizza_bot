#Pizza bot program
import random
from random import randint

#list of random names
names = ["Michael", "Jess", "Lynux", "Mikaela", "Trevor", "Sarah", "Jake", "Caitlyn", "Carlos", "Elizabeth"]
#Customer detail dictionary 
customer_details = {}

#Validtes inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid: 
        response = input (question)
        if response != "":
            return response.title() 
        else:
            print ("This cannot be blank")




# Welcome message with random name
def welcome():
    """
Purpose: To generate a random name from the list and print out a welcome message 
Parameters: None 
Returns: None

    """
    
    
    num = randint(0,9)
    name = (names[num])
    print("** Welcome to Dream Pizza **")
    print("** My name is",name,"**")
    print("** I will be here to help you order your delicious Dream Pizza **")


  




# Menu for pickup or delivery 
def order_type():
    print ("Is your order for pickup or delivery?")
    print (" For pickup enter 1.")
    print (" For delivery enter 2.")
    while True:
        try:
            delivery = int(input ("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Pickup")
                    break

                elif  delivery == 2:
                    print ("Delivery")
                    break
            else: 
                print ("Number must be 1 or 2")
        except ValueError:
            print ("That is not a valid number.")
            print ("Please enter 1 or 2.")



# Pick up information - name and phone number
def pickup():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )
    #print (customer_details ['name'])

    question = ("Please enter your phone number ")
    customer_details["phone"] = not_blank(question )
    #print (customer_details ['phone'])
    print(customer_details)




# Delivery information  - name, address and phone number





# Choose total number of Pizzas - max 5 






# Pizza menu






# Pizza ordering - from menu - print each pizza ordered with cost 





# Print order out - including if order is delivering or pick up and names and price of each pizza - total cost including any delivery charge 




# Ability to cancel or proceed with order 





# Option for new order or to exit 







# Main function 
def main():
    
    """
    Purpose:To run all functions
    Parameters: None 
    Returns: None

    """
    welcome()
    order_type()
    pickup()


main()