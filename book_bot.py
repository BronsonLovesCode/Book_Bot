import random
from random import randint

#List of random names
names = ["Bronson", "Adam", "Alain", "Ethan", "Eardwulf", "Santiago", "Daniel", "Dannell", "Luka", "Jason"]

def welcome():
    '''
    Purpose: To generate a random name from the list and print out
    a welcome message
    Parameters: None
    Returns: None

    '''
    num = randint(0,9)
    name = (names[num])
    print("Welcome to COMTIC!")
    print()
    print("My name is",name,)
    print()
    print("I will be here to help you order your ideal book.")

# Menu so that users can choose either pickup or delivery

def order_type():
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

main()