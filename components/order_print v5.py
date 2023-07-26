# List to store ordered books
order_list = ['Batman: The Killing Joke - Alan Moore','Spider-Man: Fake Red - Yusuke Osawa','Guardians of the Galaxy #1 - Collin Kelly, Jackson Lanzing',
               'The Art of War - Sun Tzu']

# List to store book prices
order_cost = [3.50, 3.50, 3.50, 13.50]

def print_order():
    total_cost = sum(order_cost)
    print("*** Customer Details ***")
    cust_details = {'name':'Mark', 'phone':'1221223452', 'house':'45', 'street':'Barry', 'suburb':'Howick'}
    print(f"Name: {cust_details['name']} \nPhone number: {cust_details['phone']} \nAddress: {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")
    print()
    print("*** Order Details ***")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("*** Total Order Cost ***")
    print(f"${total_cost:.2f}")

print_order()