#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import os
import json
import datetime
from requests import get, ConnectionError
from hashlib import md5
from dotenv import load_dotenv

os.chdir('..')
load_dotenv()
PUBLIC_KEY  = os.getenv('PUBLIC_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
COMICID = 46749

"""
The Comics Test

Your task is to generate an HTML page that lists the characters from a
Marvel-story.

Using the Marvel API [http://developer.marvel.com/docs], pick a random story
featuring your favourite character (perhaps The Hulk?). Generate an HTML page
with the following characteristics:

 * The story's description
 * A list of names and pictures of the characters that features in the story
 * The Marvel attribution text
"""

def getStory():
    """Get one story from Marvel API."""
    ts = datetime.datetime.now().timestamp()
    strHash = '{}{}{}'.format(ts, PRIVATE_KEY, PUBLIC_KEY)
    myHash = md5(strHash.encode('utf-8')).hexdigest()
    base_url = 'https://gateway.marvel.com/v1/public/comics/' + str(COMICID)
    auth_params = '?ts={}&apikey={}&hash={}'.format(ts, PUBLIC_KEY, myHash)

    try:
        response = get(base_url+auth_params)
    except ConnectionError:
        return 'Connection Error', 500

    return json.loads(response.text)
