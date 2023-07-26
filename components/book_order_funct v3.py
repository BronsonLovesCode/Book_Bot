# Book list
book_names = ['Batman: The Killing Joke - Alan Moore','Spider-Man: Fake Red - Yusuke Osawa','Guardians of the Galaxy #1 - Collin Kelly, Jackson Lanzing',
               'Mad Max: Fury Road - George Miller, Nico Lathouris, Mark Sexton','Lady Snowblood, Vol. 4: Retribution, Part 2 - Kazuo Koike',
               'Ghost in the Shell: Stand Alone Complex, Vol. 3: White Maze - Junichi Fujisaku','Watchmen - Alan Moore',
               'The Art of War - Sun Tzu','The Epic of Gilgamesh - Sin-Leqi-Unninni','Divine Comedy - Dante Alighieri','Les Miserables - Victor Hugo','The Bible - Unknown']

#Price list
book_prices = [3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 13.50, 13.50, 13.50, 13.50, 13.50]

# List to store ordered books
order_list = []

# List to store book prices
order_cost = []

#List to store order cost
def menu():
    number_books = 12

    for count in range (number_books):
        print("{} {} ${:.2f}" .format(count+1,book_names[count],book_prices[count]))

menu()

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
                    print("*** ORDER MUST BE BETWEEN 1 and 7 *** ")
            except ValueError:
                print("*** INVALID INPUT ***")
                print("Please enter a number between 1 and 7. ")
        books_ordered = books_ordered -1
        order_list.append(book_names[books_ordered])
        order_cost.append(book_prices[books_ordered])
        print("{} ${:.2f}" .format(book_names[books_ordered],book_prices[books_ordered]))
        num_books = num_books-1

print(order_list)
print(order_cost)