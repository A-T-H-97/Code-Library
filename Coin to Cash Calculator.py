#this code is a calculator to help you figure
#out how many dollars all that loose change is worth

def coin_to_cash():

    print("Break open the piggy bank for a change?\n"
          "Tell me how many of each coin you found and i'll tell you how much your treasure is worth")

    while True:
        try:
            quarters = int(input("How many quarters (25¢): "))
        except ValueError:
            print("Sorry, input must be a positive number")
            continue
        if quarters < 0:
            print("Sorry, negative numbers are not allowed")
            continue
        else:
            break

    while True:
        try:
            dimes = int(input("How many dimes (10¢): "))
        except ValueError:
            print("Sorry, input must be a positive number")
            continue
        if dimes < 0:
            print("Sorry, negative numbers are not allowed")
            continue
        else:
            break

    while True:
        try:
            nickles = int(input("How many nickles (5¢): "))
        except ValueError:
            print("Sorry, input must be a positive number")
            continue
        if nickles < 0:
            print("Sorry, negative numbers are not allowed")
            continue
        else:
            break

    while True:
        try:
            pennies = int(input("How many pennies (1¢): "))
        except ValueError:
            print("Sorry, input must be a positive number")
            continue
        if pennies < 0:
            print("Sorry, negative numbers are not allowed")
            continue
        else:
            break

    sum = float(quarters * 0.25) + float(dimes * 0.1) + float(nickles * 0.05) + float(pennies * 0.01)

    print("Huzzah! your piggy held for you " + str(round(sum, 2)) + "$")

def main():
    while True:
        conv_or_quit = input("Press 1 to start calculation, q to quit out: ")

        if conv_or_quit == '1':
            coin_to_cash()

        elif conv_or_quit == 'q':
            print("Goodbye.")
            break

        else:
             print("Invalid input.")

print("This program helps you figure out how much your change is worth")

main()