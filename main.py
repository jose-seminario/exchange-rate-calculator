from menu import (
    show_main_menu,
    show_conversion_direction,
    show_result
    )

from validation import (
    get_user_option,
    get_conversion_direction,
    get_amount
    )

from converter import (
    get_exchange_rate,
    convert_currency
    )

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
        exchange_rate = get_exchange_rate(selected_option)

        converted_amount = convert_currency(selected_direction, amount, exchange_rate)

        show_result(converted_amount)

