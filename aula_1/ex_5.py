import requests

DOMAIN_URL = 'https://gen-net.herokuapp.com/api/users/{}'

name = input ( 'digite seu nome:' )
email = input ('digite seu email')
password = input ('digite sua senha')
user_id = input ('digite seu id')

payload = {
    'name': name,
    'email': email,
    'password': password
}

response = requests.put(DOMAIN_URL.format(user_id),payload)

if response.status_code == 200:
    print ('usuário ataulizado com sucesso')
else:
    print ('erro ao atualizar o usuario')