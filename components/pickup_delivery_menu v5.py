# Menu so that users can choose either pickup or delivery

print ("Is your order for pickup or delivery?")
print()
print ("For pickup, enter 1.")
print ("For delivery, enter 2.")

while True:
      try:
            delivery = int(input("Please enter a number. "))
            if delivery >= 1 and delivery <= 2:
                  if delivery == 1:
                        print ("Pickup")
                        break

                  elif delivery == 2:
                        print ("Delivery")
                        break
            else:
                  print ("Number must be 1 or 2.")
      except ValueError:
            print ("*** INVALID INPUT ***")
            print ("Please enter 1 or 2. ")
