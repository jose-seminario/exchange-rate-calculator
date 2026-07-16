def get_user_option():

    while True:

        user_option = input("> ")

        if user_option in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")

    return user_option

def get_conversion_direction():

    while True:

        direction = input("> ")

        if direction in ["1", "2"]:
            break

        print()
        print("Invalid option. Please choose 1 or 2.")
        print()

    return direction

def get_amount():

    while True:

        amount = input("Enter the amount: ")

        try:
            amount = float(amount)
            break

        except:
            print()
            print("Invalid amount. Please enter a valid number.")
            print()

    return amount