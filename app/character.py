import os
import json
import datetime
from requests import get, ConnectionError
from hashlib import md5
from app import auth

auth.setup()

PUBLIC_KEY  = os.getenv('PUBLIC_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')

def getCharacter(id):
    """Get character by id from Marvel API."""

    ts = datetime.datetime.now().timestamp()
    strHash = '{}{}{}'.format(ts, PRIVATE_KEY, PUBLIC_KEY)
    myHash = md5(strHash.encode('utf-8')).hexdigest()
    base_url = 'https://gateway.marvel.com/v1/public/characters/' + str(id)
    auth_params = '?ts={}&apikey={}&hash={}'.format(ts, PUBLIC_KEY, myHash)

    try:
        response = get(base_url+auth_params)
    except ConnectionError:
        return 'Connection Error', 500

    return json.loads(response.text)
