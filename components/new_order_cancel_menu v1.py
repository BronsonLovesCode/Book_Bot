print ("Do you wish to start another order or exit?")
print ("To start another order, enter 1.")
print ("To exit the BOT, enter 2. ")

while True:
      try:
            confirm = int(input("Please enter a number. "))
            if confirm >= 1 and confirm <= 2:
                  if confirm == 1:
                        print ("*** NEW ORDER ***")
                        break

                  elif confirm == 2:
                        print ("*** EXITING BOT ***")
                        break
            else:
                  print ("*** NUMBER MUST BE 1 OR 2*** ")
      except ValueError:
            print ("*** INVALID INPUT ***")
            print ("Please enter 1 or 2. ")