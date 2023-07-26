# Bugs
# Will only work for valid input "d" and "p"

# Menu so that users can choose either pickup or delivery

print ("Do you want to pickup your order or do you want it delivered to you?")
print()
print ("For pickup, enter p. For delivery, enter d. ")

delivery = input()

if delivery == "p":
     print ("Pickup")

elif delivery == "d":
     print ("Delivery")
