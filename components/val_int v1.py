def order_type(low, high, question):
    while True:
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                print (f"Please enter a number between {low} and {high}.")
        except ValueError:
            print ("*** INVALID INPUT ***")
            print ()
            print (f"Please enter a number between {low} and {high}. ")
                
LOW = 1
HIGH = 12
question = (f"Enter a number between {LOW} and {HIGH}. ")

answer = order_type(LOW, HIGH, question)

print(answer)