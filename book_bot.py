import random
from random import randint



# Name list
names = ["Bronson", "Adam", "Alain", "Ethan", "Eardwulf", "Santiago", "Daniel", "Dannell", "Luka", "Jason"]



# Customer details dictionary
customer_details = {}



# Blank input validator
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response
        else:
            print ()
            print ("*** BLANK INPUT ***")
            print ()



# Welcome message
def welcome():
    '''
    Purpose: To generate a random name from the list and print out
    a welcome message
    Parameters: None
    Returns: None

    '''
    num = randint(0,9)
    name = (names[num])
    print ("Welcome to COMTIC!")
    print ("My name is",name,)
    print ("I will be here to help you order your ideal book.")
    print ()



# Menu for pickup or delivery
def order_type():
    print ("Is your order for pickup or delivery?")
    print ("For pickup, enter 1.")
    print ("For delivery, enter 2.")
    while True:
        try:
                delivery = int(input("Please enter a number. "))
                if delivery >= 1 and delivery <= 2:
                    if delivery == 1:
                            print ("Pickup")
                            print ()
                            break

                    elif delivery == 2:
                            print ("Delivery")
                            print ()
                            break
                else:
                    print ()
                    print ("Number must be 1 or 2.")
                    print ()
        except ValueError:
                print ()
                print ("*** INVALID INPUT ***")
                print ()
                print ("Please enter 1 or 2. ")
                print ()



# Pickup information - name and phone number
def pickup_info():
    question = ("Please enter your name. ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])
    print ()

    question = ("Please enter your phone number. ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])
    print ()
    print(customer_details)



# Main function
def main():
    '''
    Purpose: To run all functions
    a welcome message
    Parameters: None
    Returns: None

    '''
    welcome()
    order_type()
    pickup_info()

main()