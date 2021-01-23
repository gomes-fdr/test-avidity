from flask import Flask
from flask import render_template
from .story import getStory

app = Flask(__name__)

@app.route('/')
def index():

    try:
        story = getStory()
    except:
        return 'Connection Error', 500

    return render_template('index.html')
