import requests

URL = "http://viacep.com.br/ws/{}/json"

CEP = input('Digite seu CEP')
response = requests.get(URL.format(CEP))
print(response.json())