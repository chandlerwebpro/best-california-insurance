import requests

url = 'https://5c71376c-5f5d-40b6-9f7b-75a397d404e0.quotes.iwantinsurance.com/(X(1)S(hjw31k0x4ibehmwa4mt4s0x0))/LocalTerrHelp.asmx/GetRegions'
data = {"knownCategoryValues":"County,CA,90746:LOS ANGELES;City,CA,90746:CARSON;","category":"Region,CA,90746"}

r = requests.post(url, json=data)
print(r.text)