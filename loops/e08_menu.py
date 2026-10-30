from time import sleep
while True:
    try:
        user = int(input(f"{"=-" * 10} {"MENU":^10}{"=-" * 10}\n1 - Print Hello\n2 - Print Good bye\n3 - Leave\n{"=-" * 10}\nYour choice: "))
        print("=-" * 10)
        if user < 0 or user >3 :
            print("ERROR! Type a valid option.")
    except ValueError:
        print("ERROR! Invalid Value, please try again.")
    except KeyboardInterrupt:
        print("ERROR! Invalid input, please type ona of the options given.")
    else:
        if user == 1:
            print("Hello")
        elif user == 2:
            print("Good bye")
        elif user == 3:
            print("Come back soon ! :)")
            break
    sleep(1)
        