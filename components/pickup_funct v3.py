# Customer details dictionary
customer_details = {}

# Basic instructions
print("Please enter the pickup information.")

# Customer name not blank
valid = False
while not valid:
    customer_details['name'] = input("Please enter your name. ")
    if customer_details['name'] != "":
        print(customer_details['name'])
        break

    else:
        print("*** NAME CAN NOT BE BLANK ***")

# Customer phone number not blank
valid = False
while not valid:
    customer_details['phone'] = input("Please enter your phone number. ")
    if customer_details['phone'] != "":
        print(customer_details['phone'])
        break

    else:
        print("*** PHONE NUMBER CAN NOT BE BLANK ***")

print(customer_details)