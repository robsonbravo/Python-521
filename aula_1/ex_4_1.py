import requests
url = 'https://gen-net.herokuapp.com/api/users/'
res = requests.get(url)

users = res.json()

email = input ('digite seu email ')

for user in users:
    if user.get ('email') == email:
        print(user) 