# Test avidity
To consume the Marvel API.

## The Comics Test

Your task is to generate an HTML page that lists the characters from a
Marvel-story.

Using the Marvel API [http://developer.marvel.com/docs], pick a random story
featuring your favorite character (perhaps The Hulk?). Generate an HTML page
with the following characteristics:

 * The story's description
 * A list of names and pictures of the characters that features in the story
 * The Marvel attribution text

## About this project
I use the follow stack:

* Python 3.6
* Python Flask
* Python requests

## Instructions

0. Make a clone from:

 `git clone https://github.com/gomes-fdr/test-avidity.git`

1. Replace the file `app/auth.py` by the file that I email you.
2. Create a virtual env inside the project folder to protect your
 environment sanity:

    `python -m venv .venv`

3. Active that environment: `source .venv/bin/activate`
4. Run `pip install -r requirements.txt` to install the dependencies.
5. Run in the terminal `flask run`.

After this steps you should see the message:

```
* Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Open a web browser and point to: `http://127.0.0.1:5000/`

## Note
The story that I choose, unfortunately, didn't have the list of characters. Then I decide put the characters that I remember.
