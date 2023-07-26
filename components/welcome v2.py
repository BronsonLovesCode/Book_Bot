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

def main():
    '''
    Purpose: To run all functions
    a welcome message
    Parameters: None
    Returns: None

    '''
    welcome()

main()