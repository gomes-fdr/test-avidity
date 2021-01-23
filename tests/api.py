"""A simple test of connection to marvel API."""
import os
from requests import get
from hashlib import md5
from dotenv import load_dotenv

os.chdir('..')
load_dotenv()
PUBLIC_KEY = os.getenv('PUBLIC_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')

print('chave publica: {}'.format(PUBLIC_KEY))

ts = 1
strHash = '{}{}{}'.format(ts, PRIVATE_KEY, PUBLIC_KEY)
myHash = md5(strHash.encode('utf-8')).hexdigest()
base_url = 'https://gateway.marvel.com/v1/public/comics'
auth_params = '?ts={}&apikey={}&hash={}'.format(ts, PUBLIC_KEY, myHash)

print(base_url+auth_params)
response = get(base_url+auth_params)

assert response.status_code == 200, 'Erro ao buscar infos da API'
