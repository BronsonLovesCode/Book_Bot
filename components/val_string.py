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
            break

question = "Please enter your name. "
name = check_string(question)
print(name)