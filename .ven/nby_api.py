import requests

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for currency in data:
        print(f"{currency['cc']} - {currency['rate']} грн")
else:
    print(f"Помилка запиту: {response.status_code}")
