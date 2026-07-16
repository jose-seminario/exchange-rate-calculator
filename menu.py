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

def show_conversion_direction():
    print()
    print("Choose a conversion direction")
    print("1. USD → PEN")
    print("2. PEN → USD")
    print()

def show_result(converted_amount):
    print()
    print("The converted amount is:", converted_amount)
    print()
