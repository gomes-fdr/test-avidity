from requests import get
from hashlib import md5

public_key = 'e04f3ae80a4e5d20d1177f0159f1b367'
private_key = '37c97b78f13da604afee9b9bb4ae8922af8b2697'
ts = 1
strHash = '{}{}{}'.format(ts, private_key, public_key)
myHash = md5(strHash.encode('utf-8')).hexdigest()
base_url = 'https://gateway.marvel.com/v1/public/comics'
auth_params = '?ts={}&apikey={}&hash={}'.format(ts, public_key, myHash)

print(base_url+auth_params)
response = get(base_url+auth_params)

assert response.status_code == 200, 'Erro ao buscar infos da API'
