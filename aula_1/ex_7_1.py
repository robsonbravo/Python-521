import requests

DOMAIN_URL = 'https://gen-net.herokuapp.com/api/users/'

payload = {
'name' : input ( 'digite seu nome:' ),
'email' : input ('digite seu email'),
'password' : input ('digite sua senha')
}

res = requests.post(DOMAIN_URL, payload)

if res.status_code == 200:
    user_id = res.json().get ('id')
    print ('Usuario {} criado com sucesso'.format(user_id))
else:
    print (res.text)