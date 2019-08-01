import requests
user = input ('digite seu usuario')
url = 'https://gen-net.herokuapp.com/api/users/'
response = requests.get(url.format(user))
print(response.json())