print("Please enter the pickup information.")

# Customer name
valid = False
while not valid:
    name = input("Please enter your name. ")
    if name != "":
        print(name)
        break

    else:
        print("*** NAME CAN NOT BE BLANK ***")

# Customer phone number
valid = False
while not valid:
    phone = input("Please enter your phone number. ")
    if phone != "":
        print(phone)
        break

    else:
        print("*** PHONE NUMBER CAN NOT BE BLANK ***")