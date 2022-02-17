#Pizza bot program
import random
from random import randint

#list of random names
names = ["Michael", "Jess", "Lynux", "Mikaela", "Trevor", "Sarah", "Jake", "Caitlyn", "Carlos", "Elizabeth"]

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






# Pick up information - name and phone number






# Delivery information  - name, address and phone number





# Choose total number of Pizzas - max 5 






# Pizza menu






# Pizza ordering - from menu - print each pizza ordered with cost 





# Print order out - including if order is delivering or pick up and names and price of each pizza - total cost including any delivery charge 




# Ability to cancel or proceed with order 





# Option for new order or to exit 







# Main function 
def main():
    welcome()
    """
    Purpose:To run all functions
    Parameters: None 
    Returns: None

    """


main()