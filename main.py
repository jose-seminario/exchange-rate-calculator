def show_main_menu():
    print("=" * 42)
    print("|  Exchange Rate Calculator  |")
    print("=" * 42)
    print()

    print("Welcome! Select a currency pair to continue.")
    print()

    print("1. USD ↔ PEN")
    print("2. EUR ↔ PEN")
    print("3. USD ↔ EUR")
    print("4. GBP ↔ PEN")
    print("5. Exit")

    print()
    print("Choose an option")


def get_user_option():
    user_option = input("> ")
    return user_option


def show_conversion_direction():
    print()
    print("Choose a conversion direction")
    print("1. USD → PEN")
    print("2. PEN → USD")
    print()


def get_conversion_direction():
    direction = input("> ")
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


def convert_currency(selected_option, selected_direction, amount, exchange_rate):
    if selected_direction == "1":
        amount = amount * exchange_rate
    else:
        amount = amount / exchange_rate

    return amount


def show_result(converted_amount):
    print()
    print("The converted amount is:", converted_amount)
    print()


# ==========================
# Main Program
# ==========================

selected_option = ""

while selected_option != "5":

    show_main_menu()

    selected_option = get_user_option()

    if selected_option == "5":
        print()
        print("Goodbye!")
        print("Thank you for using the program!")

    elif selected_option in ["1", "2", "3", "4"]:

        show_conversion_direction()

        selected_direction = get_conversion_direction()

        amount = get_amount()

        # Temporary exchange rate (later it will come from an API)
        exchange_rate = 3.40

        converted_amount = convert_currency(
            selected_option,
            selected_direction,
            amount,
            exchange_rate
        )

        show_result(converted_amount)

    else:
        print()
        print("Invalid option. Please try again.")
        print()
        