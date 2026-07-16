import requests

def get_exchange_rate(selected_option):

    if selected_option == "1":
        base_currency = "USD"
        target_currency = "PEN"

    elif selected_option == "2":
        base_currency = "EUR"
        target_currency = "PEN"

    elif selected_option == "3":
        base_currency = "USD"
        target_currency = "EUR"

    elif selected_option == "4":
        base_currency = "GBP"
        target_currency = "PEN"

    url = f"https://open.er-api.com/v6/latest/{base_currency}"

    try:

        response = requests.get(url)

        exchange_data = response.json()

        exchange_rate = exchange_data["rates"][target_currency]

        return exchange_rate

    except:

        return None

def convert_currency(selected_direction, amount, exchange_rate):
    if selected_direction == "1":
        amount = amount * exchange_rate
    else:
        amount = amount / exchange_rate

    return amount
