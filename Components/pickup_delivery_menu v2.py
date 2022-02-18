# Bugs
# Will only work for valind input "d" "p"
# Invalid input triggers else statement but program does not ask for input again 
# menu so that choose either pickup or delviery 

print ("Do you want your order delivered or are you picking it up?")

print (" For delivery enter d.")
print (" For pickup enter p.")
delivery = input ()
if delivery == "d":
    print ("Delviery")


elif  delivery == "p":
    print ("Pickup")

else:
    print ("That was not a valid input.")



