import random
from random import randint



# Name list
names = ["Bronson", "Adam", "Alain", "Ethan", "Eardwulf", "Santiago", "Daniel", "Dannell", "Luka", "Jason", "Denzelle"]



# Book list
book_names = ['Batman: The Killing Joke - Alan Moore','Spider-Man: Fake Red - Yusuke Osawa','Guardians of the Galaxy #1 - Collin Kelly, Jackson Lanzing',
               'Mad Max: Fury Road - George Miller, Nico Lathouris, Mark Sexton','Lady Snowblood, Vol. 4: Retribution, Part 2 - Kazuo Koike',
               'Ghost in the Shell: Stand Alone Complex, Vol. 3: White Maze - Junichi Fujisaku','Watchmen - Alan Moore',
               'The Art of War - Sun Tzu','The Epic of Gilgamesh - Sin-Leqi-Unninni','Divine Comedy - Dante Alighieri','Les Miserables - Victor Hugo','The Bible - Unknown']



# Price list
book_prices = [3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 13.50, 13.50, 13.50, 13.50, 13.50]



# List to store ordered books
order_list = []



# List to store book prices
order_cost = []



# Customer details dictionary
customer_details = {}



# Blank input validator
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
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
                            pickup_info()
                            del_pick = "pickup"
                            break

                    elif delivery == 2:
                            print ("Delivery")
                            delivery_info()
                            del_pick = "delivery"
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
    return (del_pick)


# Pickup information - name and phone number
def pickup_info():
    print()
    question = ("Please enter your name. ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])
    print ()

    question = ("Please enter your phone number. ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])
    print ()
    print(customer_details)



# Delivery information - name, phone number, and address
def delivery_info():
    print()
    question = ("Please enter your name. ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])

    question = ("Please enter your phone number. ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])

    question = ("Please enter your house number. ")
    customer_details['house'] = not_blank(question)
    print (customer_details['house'])

    question = ("Please enter your street name. ")
    customer_details['street'] = not_blank(question)
    print (customer_details['street'])

    question = ("Please enter your suburb. ")
    customer_details['suburb'] = not_blank(question)
    print (customer_details['suburb'])
    print (customer_details)



# Book menu
def menu():
    number_books = 12

    for count in range (number_books):
        print("{} {} ${:.2f}" .format(count+1,book_names[count],book_prices[count]))



# Choose total number of books - max 7
# Book order - from menu - print each book ordered with cast
def order_books():
# Ask for total number of books for order
    num_books = 0

    while True:
        try:
            num_books = int(input("How many books do you wish to order? "))
            if num_books >= 1 and num_books <= 7:
                break
            else:
                print("*** ORDER MUST BE BETWEEN 1 and 7 *** ")
        except ValueError:
            print("*** INVALID INPUT ***")
            print("Please enter a number between 1 and 7. ")


    print(num_books)

# Choose books from menu
    for item in range(num_books):
        while num_books > 0:
            while True:
                try:
                    books_ordered = int(input("Please choose your book(s) by entering the corresponding number from the menu. "))
                    if books_ordered >= 1 and books_ordered <= 12:
                        break
                    else:
                        print("*** ORDER MUST BE BETWEEN 1 AND 7 *** ")
                except ValueError:
                    print("*** INVALID INPUT ***")
                    print("Please enter a number between 1 and 7. ")
            books_ordered = books_ordered -1
            order_list.append(book_names[books_ordered])
            order_cost.append(book_prices[books_ordered])
            print("{} ${:.2f}" .format(book_names[books_ordered],book_prices[books_ordered]))
            num_books = num_books-1



# Print order out - Including if order is delivery or pickup and names and price of each book - total cost including any delivery charge
def print_order(del_pick):
    total_cost = sum(order_cost)
    print()
    print("*** CUSTOMER DETAILS ***")
    if del_pick == "delivery":
        print("Your order is for delivery. A $3.00 dollar delivery charge applies.")
        total_cost = total_cost + 3
        print(f"Name: {customer_details['name']} \nPhone number: {customer_details['phone']} \nAddress: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    elif del_pick == "pickup":
        print("Your order is for pickup")
        print(f"Name: {customer_details['name']} \nPhone number: {customer_details['phone']}")
    print()
    print("*** ORDER DETAILS ***")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("*** TOTAL ORDER COST ***")
    print(f"${total_cost:.2f}")
    print()

# Main function
def main():
    '''
    Purpose: To run all functions
    a welcome message
    Parameters: None
    Returns: None

    '''
    welcome()
    del_pick = order_type()
    menu()
    order_books()
    print_order(del_pick)

main()