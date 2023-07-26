# Print order out - Including if order is delivery or pickup and names and price of each book - total cost including any delivery charge
def print_order(del_pick):
    total_cost = sum(order_cost)
    print()
    print("*** Customer Details ***")
    if del_pick == "delivery":
        print("Your order is for delivery. A $3.50 dollar delivery charge applies.")
        total_cost = total_cost + 5
        print(f"Name: {cust_details['name']} \nPhone number: {cust_details['phone']} \nAddress: {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")
    elif del_pick == "pickup":
        print("Your order is for pickup")
        print(f"Name: {cust_details['name']} \nPhone number: {cust_details['phone']}")
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