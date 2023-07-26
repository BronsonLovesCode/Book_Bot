# Bugs
# Will only work for valid input "d" and "p"
# Invalid input triggers else statement, but program does not ask for input again
# Menu so that users can choose either pickup or delivery

print ("Do you want to pickup your order or do you want it delivered?")
print()
print ("For pickup, enter p.")
print ("For delivery, enter d. ")

delivery = input()

if delivery == "p":
     print ("Pickup")

elif delivery == "d":
     print ("Delivery")

else:
     print ("*** INVALID INPUT ***")
