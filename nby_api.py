import requests

def get_exchange_rates():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Не вдалося отримати дані.")
        return None

def find_rate(data, currency_code):
    for currency in data:
        if currency['cc'] == currency_code:
            return currency['rate']
    return None

def convert_currency(amount, from_currency, to_currency, rates):
    # Якщо гривня, то курс = 1 (НБУ дає курс щодо гривні)
    if from_currency == "UAH":
        from_rate = 1
    else:
        from_rate = find_rate(rates, from_currency)
    if to_currency == "UAH":
        to_rate = 1
    else:
        to_rate = find_rate(rates, to_currency)

    if from_rate is None or to_rate is None:
        print("Невідома валюта.")
        return None

    # Конвертація через гривню
    amount_in_uah = amount * from_rate
    converted_amount = amount_in_uah / to_rate
    return converted_amount

def main():
    rates = get_exchange_rates()
    if not rates:
        return

    amount = float(input("Введіть суму: "))
    from_currency = input("З якої валюти (код, напр. USD): ").upper()
    to_currency = input("У яку валюту (код, напр. EUR): ").upper()

    result = convert_currency(amount, from_currency, to_currency, rates)
    if result:
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")

if __name__ == "__main__":
    main()
