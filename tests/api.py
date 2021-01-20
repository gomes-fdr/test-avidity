import requests

token = 'e04f3ae80a4e5d20d1177f0159f1b367'
base_url = 'https://gateway.marvel.com/v1/public/comics'
header = {'Authorization': 'token {}'.format(token)}

response = requests.get(base_url, headers=header)

assert response.status_code == 200, 'Erro ao buscar infos da API'

