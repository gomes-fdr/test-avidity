from flask import Flask
from flask import render_template
from .story import getStory
from .character import getCharacter

app = Flask(__name__)

COMICID = 46749
WOLVERINE: 1009718
SABRETOOTH: 1009554

@app.route('/')
def index():
    characters = []

    try:
        story = getStory(COMICID)
    except:
        return 'Connection Error', 500

    try:
        wolverine = getCharacter(1009718)
        characters.append(wolverine)
    except:
        return 'Connection Error', 500

    try:
        sabretooth = getCharacter(1009554)
        characters.append(sabretooth)
    except:
        return 'Connection Error', 500


    return render_template('index.html', story=story, characters=characters)
