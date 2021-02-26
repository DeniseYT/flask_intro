"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
    <html>Hi! This is the home page.
    <a href= "/hello"> "Click here" </a>
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/hello">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
          <label>How would you like to be compliment?</label>
          <input type="radio" name="title" value="Mr."> Mr.
          <input type="radio" name="title" value="Mrs."> Mrs.
          <input type="radio" name="title" value="Miss."> Miss
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""
    title = request.args.get("title")
    player = request.args.get("person")

    compliment = choice(AWESOMENESS)
    
    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {title} {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(title, player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")


