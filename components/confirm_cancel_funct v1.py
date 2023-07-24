print ("Please confirm your order.")
print ("To confirm order, enter 1.")
print ("To cancel order, enter 2.")
print ()

while True:
      try:
            confirm = int(input("Please enter a number. "))
            if confirm >= 1 and confirm <= 2:
                  if confirm == 1:
                        print ("Order confirmed")
                        break

                  elif confirm == 2:
                        print ("Order cancelled")
                        break
            else:
                  print ("*** NUMBER MUST BE 1 OR 2 *** ")
                  print ()
      except ValueError:
            print ("*** INVALID INPUT ***")
            print ()
            print ("Please enter 1 or 2. ")