print ("Please confirm your order.")
print ("To confirm order, enter 1.")
print ("To cancel order, enter 2.")
print ()

while True:
      try:
            confirm = int(input("Please enter a number. "))
            if confirm >= 1 and confirm <= 2:
                  if confirm == 1:
                        print ()
                        print ("*** ORDER CONFIRMED ***")
                        print ()
                        print ("Your order has been sent to our store to be prepared,")
                        print ("your book(s) will be with you shortly!")
                        print ()
                        break

                  elif confirm == 2:
                        print ()
                        print ("*** ORDER CANCELLED ***")
                        print ()
                        print ("You can restart your order or exit the BOT.")
                        print ()
                        break
            else:
                  print ("*** NUMBER MUST BE 1 OR 2 *** ")
      except ValueError:
            print ("*** INVALID INPUT ***")
            print ()
            print ("Please enter 1 or 2. ")
            print ()