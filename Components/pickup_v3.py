#Customer detail dictionary 
customer_details = {}


#Basic Instructions 
print ("Please enter the pickup information")

#customer name
valid = False 
while not valid:
    customer_details["name"] = input ("Please enter your name ")
    if customer_details["name"] != "":
        print (customer_details["name"])
        break 

    else:
        print("Sorry this cannot be blank")


#customers phone number
valid = False 
while not valid: 
    customer_details["phone"] = input("Please enter your phone number ")
    if customer_details["phone"] != "":
        print (customer_details["phone"])
        break 
    else:
        print("Sorry this cannot be blank")

print (customer_details)
