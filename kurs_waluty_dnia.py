import requests
print ("Sprawdź historyczny kurs waluty. Dane od 2 stycznia 2002 r.")

code = input("Wprowadź trzyliterowy kod waluty zgodny ze standardem ISO 4217: ")
print("Standard ISO można znaleźć tutaj: https://pl.wikipedia.org/wiki/ISO_4217#Kody_w_u%C5%BCyciu")
date = input("Podaj datę w formacie YYYY-MM-DD: ")

url = f'http://api.nbp.pl/api/exchangerates/rates/a/{code}/{date}/'

resp = requests.get(url)
data = resp.json()
exchange_rate = data["rates"][0]["mid"]

print(f"1 {code} to {exchange_rate} PLN w dniu {date}")


