
print ("Please confirm your order")
print (" To confirm please enter 1.")
print (" To cancel please enter 2.")


low = 1
high = 2


while True:
    try:
        confirm = int(input ("Please enter a number "))
        if confirm >= 1 and confirm <= 2:
         if confirm == 1:
            print ("Order Confirmed")
            print ("Your order has been sent to our kitchen")
            print ("Your delicious pizza will be with you shortly")
            break

         elif  confirm == 2:
             print ("Your order has been cancelled")
             print ("You can restart your order or exit the Bot")
             break
        else: 
            print ("Number must be 1 or 2")
    except ValueError:
        print ("That is not a valid number.")
        print ("Please enter 1 or 2.")