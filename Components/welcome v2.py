import random
from random import randint

#list of random names
names = ["Michael", "Jess", "Lynux", "Mikaela", "Trevor", "Sarah", "Jake", "Caitlyn", "Carlos", "Elizabeth"]

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

def main():
    welcome()
    """
    Purpose:To run all functions
    Parameters: None 
    Returns: None

    """


main()