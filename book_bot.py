# Book bot
"""This file makes up the code for an ordering bot for books."""
import sys
from random import randint
# Contestants
low = 1
high = 2

# Name list
names = ["Bronson", "Adam", "Alain",
         "Ethan", "Eardwulf", "Santiago",
         "Daniel", "Dannell", "Luka",
         "Jason", "Denzelle", "Chanel"]

# Book list
book_names = ['Batman: The Killing Joke',
              'Spider-Man: Fake Red',
              'Guardians of the Galaxy #1',
              'Mad Max: Fury Road',
              'Lady Snowblood, Vol. 4: Retribution, Part 2',
              'Ghost in the Shell: Stand Alone Complex, Vol. 3: White Maze',
              'Watchmen',
              'The Art of War',
              'The Epic of Gilgamesh',
              'Divine Comedy',
              'Les Miserables',
              'The Bible']

# Price list
book_prices = [3.50, 3.50, 3.50,
               3.50, 3.50, 3.50,
               3.50, 13.50, 13.50,
               13.50, 13.50, 13.50]

# List to store ordered books
order_list = []

# List to store book prices
order_cost = []

# Customer details dictionary
customer_details = {}


# Blank input validator
def not_blank(question):
    """Check that  what is inputed is not blank."""
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print()
            print("*** BLANK INPUT ***")
            print()


# Integer input validator
def val_int(low, high, question):
    """Check what is inputed is between a function's numbers/not an invalid."""
    while True:
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                print(f"Please enter a number between {low} and {high}. ")
        except ValueError:
            print("*** INVALID INPUT ***")
            print()


def check_string(question):
    while True:
        response = input(question)
        x = response.isalpha()
        if x == False:
            print()
            print("***INPUT MUST ONLY CONTAIN LETTERS ***")
            print()
        else:
            print(response.title())


# Welcome message
def welcome():
    """Message that welcomes user to the bot."""
    num = randint(0, 9)
    name = (names[num])
    print("Welcome to COMTIC!")
    print("My name is", name,)
    print("I will be here to help you order your ideal book.")
    print()


# Pickup/Delivery menu
def order_type():
    """Choice between pickup or delivery when ordering."""
    del_pick = ""
    question = (f"Please enter a number between {low} and {high}. ")
    print("Is your order for pickup or delivery?")
    print("Press 1 for pickup.")
    print("Press 2 for delivery.")
    delivery = val_int(low, high, question)
    if delivery == 1:
        print()
        print("*** PICKUP ***")
        del_pick = "pickup"
        pickup_info()
    else:
        print()
        print("*** DELIVERY ***")
        del_pick = "delivery"
        delivery_info()
    return (del_pick)


# Pickup information - name and phone number
def pickup_info():
    """Gather customer details for pickup."""
    print()
    question = ("Please enter your name. ")
    customer_details['name'] = check_string(question)
    print(customer_details['name'])
    print()

    question = ("Please enter your phone number. ")
    customer_details['phone'] = not_blank(question)
    print(customer_details['phone'])
    print()
    print(customer_details)


# Delivery information - name, phone number, and address
def delivery_info():
    """Gather customer details for delivery."""
    print()
    question = ("Please enter your name. ")
    customer_details['name'] = check_string(question)
    print(customer_details['name'])

    question = ("Please enter your phone number. ")
    customer_details['phone'] = not_blank(question)
    print(customer_details['phone'])

    question = ("Please enter your house number. ")
    customer_details['house'] = not_blank(question)
    print(customer_details['house'])

    question = ("Please enter your street name. ")
    customer_details['street'] = check_string(question)
    print(customer_details['street'])

    question = ("Please enter your suburb. ")
    customer_details['suburb'] = check_string(question)
    print(customer_details['suburb'])
    print(customer_details)


# Book menu
def menu():
    """Generate book menu using book names and prices."""
    number_books = 12

    for count in range(number_books):
        print("{} {} ${:.2f}" .
              format(count+1, book_names[count], book_prices[count]))


# Choose total number of books - max 7
# Book order - from menu - print each book ordered with cast
def order_books():
    """User selects how many and which books they want."""
    # Ask for total number of books for order
    num_books = 0
    num_low = 1
    num_high = 7
    menu_low = 1
    menu_high = 12
    question = (f"Enter a number between {num_low} and {num_high}. ")
    print("How many books do you wish to order? ")
    num_books = val_int(num_low, num_high, question)

# Choose books from menu
    for item in range(num_books):
        while num_books > 0:
            print()
            print("Please choose your book(s) by"
                  "entering the corresponding number(s) from the menu.")
            question = (f"Enter a number between {menu_low} and {menu_high}. ")
            books_ordered = val_int(menu_low, menu_high, question)
            books_ordered = books_ordered-1
            order_list.append(book_names[books_ordered])
            order_cost.append(book_prices[books_ordered])
            print("{} ${:.2f}" .format(book_names[books_ordered],
                                       book_prices[books_ordered]))
            num_books = num_books-1


# Print order out
# Include if order is delivery or pickup and names and price of each book
# Total cost including any delivery charge
def print_order(del_pick):
    """Print out order details for user to look through."""
    total_cost = sum(order_cost)
    print()
    print("*** CUSTOMER DETAILS ***")
    if del_pick == "delivery":
        print("Your order is for delivery."
              "A $3.00 dollar delivery charge applies.")
        total_cost = total_cost + 3
        print(f"Name: {customer_details['name']}"
              f"\nPhone number: {customer_details['phone']}"
              f"\nAddress: {customer_details['house']} "
              f"{customer_details['street']} "
              f"{customer_details['suburb']}")

    elif del_pick == "pickup":
        print("Your order is for pickup")
        print(f"Name: {customer_details['name']}"
              f"\nPhone number: {customer_details['phone']}")
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


# Cancel or proceed with order
def confirm_cancel():
    """User selects whether or not they confirm their order."""
    question = (f"Please enter a number between {low} and {high}.")
    print("Please confirm your order.")
    print("To confirm order, enter 1.")
    print("To cancel order, enter 2.")
    print()

    confirm = val_int(low, high, question)
    if confirm == 1:
        print()
        print("*** ORDER CONFIRMED ***")
        print()
        print("Your order has been sent to our store to be prepared,")
        print("your book(s) will be with you shortly!")
        print()
        new_exit()

    elif confirm == 2:
        print()
        print("*** ORDER CANCELLED ***")
        print()
        print("You can restart your order or exit the BOT.")
        print()
        new_exit()


# Option for new order/exit
def new_exit():
    """User selects whether to start another order or to exit."""
    question = (f"Please enter a number between {low} and {high}.")
    print("Do you wish to start another order or exit?")
    print("To start another order, enter 1.")
    print("To exit the BOT, enter 2. ")
    confirm = val_int(low, high, question)
    if confirm == 1:
        print("*** NEW ORDER ***")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        main()

    elif confirm == 2:
        print("*** EXIT ***")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        sys.exit()


# Main function
def main():
    """Run all functions."""
    welcome()
    del_pick = order_type()
    menu()
    order_books()
    print_order(del_pick)
    confirm_cancel()
    new_exit()


main()
