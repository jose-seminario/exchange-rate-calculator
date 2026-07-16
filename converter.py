def get_exchange_rate(selected_option):

    if selected_option == "1":
        return 3.40

    elif selected_option == "2":
        return 3.95

    elif selected_option == "3":
        return 0.92

    elif selected_option == "4":
        return 4.60

def convert_currency(selected_direction, amount, exchange_rate):
    if selected_direction == "1":
        amount = amount * exchange_rate
    else:
        amount = amount / exchange_rate

    return amount
