# Bugs
# Invalid input displays value error
# Menu so that users can choose either pickup or delivery

print ("Is your order for pickup or delivery?")
print()
print ("For pickup, enter 1.")
print ("For delivery, enter 2. ")

delivery = int(input())

if delivery == 1:
     print ("Pickup")

elif delivery == 2:
     print ("Delivery")

else:
     print ("*** INVALID INPUT ***")
