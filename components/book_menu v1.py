book_names = ['Batman: The Killing Joke - Alan Moore','Spider-Man: Fake Red - Yusuke Osawa','Guardians of the Galaxy #1 - Collin Kelly, Jackson Lanzing',
               'Mad Max: Fury Road - George Miller, Nico Lathouris, Mark Sexton','Lady Snowblood, Vol. 4: Retribution, Part 2 - Kazuo Koike',
               'Ghost in the Shell: Stand Alone Complex, Vol. 3: White Maze - Junichi Fujisaku','Watchmen - Alan Moore',
               'The Art of War - Sun Tzu','The Epic of Gilgamesh - Sin-Leqi-Unninni','Divine Comedy - Dante Alighieri','Les Miserables - Victor Hugo','The Bible - Unknown']

book_prices = [3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 13.50, 13.50, 13.50, 13.50, 13.50]

number_books = 12

def menu():
    number_books = 12

#print("How many books would you like to order? ")
#num_books = int(input())

    for count in range (number_books):
        print(count,book_names[count],book_prices[count])

menu()