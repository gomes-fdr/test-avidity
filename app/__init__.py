from flask import Flask
from flask import render_template
from .story import getStory
from .character import getCharacter

app = Flask(__name__)

COMICID = 46749
CARACTERS = [1009718, 1009554]


@app.route('/')
def index():
    characters = []

    try:
        story = getStory(COMICID)
    except:
        return 'Connection Error', 500

    for c_id in CARACTERS:
        try:
            hero = getCharacter(c_id)
        except:
            return 'Connection Error', 500

        characters.append(hero)

    return render_template('index.html', story=story, characters=characters)
