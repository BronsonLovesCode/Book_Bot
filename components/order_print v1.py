# List to store ordered books
order_list = ['Batman: The Killing Joke - Alan Moore','Spider-Man: Fake Red - Yusuke Osawa','Guardians of the Galaxy #1 - Collin Kelly, Jackson Lanzing',
               'The Art of War - Sun Tzu']



# List to store book prices
order_cost = [3.50, 3.50, 3.50, 13.50]



count = 0
for item in order_list:
    print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
    count = count+1