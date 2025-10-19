# Visit D3vd/Meme_Api on github for info about API

from flask import Flask, render_template # Render_template -- for a custom HTML file
import requests  # Interract with meme API
import json  # Use JSON functionality

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme" # API URL
    response = json.loads(requests.request("GET", url).text) # This code gets contents from the response and turns it into json
    meme_large = response["preview"][-2] # This is basically the meme picture
    subreddit = response["subreddit"] # This is the subreddit that the meme is currently generated from -- THis is because it generates from random subreddits
    return meme_large, subreddit

# A decorator is a function that takes in a function and returns a function
@app.route("/") # Decorator for index
def index():  # Decorated function
    meme_pic, subreddit = get_meme() # Meme info 

    # Render template allow Flask to use another HTML file to display
    # The HTML file e.g "meme_index.html", should be in the "templates" folder
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit) # Passing in arguments that will be used in the HTML file

if __name__ == "__main__":
    app.run(debug=True) # Debug mode - No need for reloading
