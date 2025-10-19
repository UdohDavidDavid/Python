# Visit geeksforgeeks for flask tutorial

# Data types in Flask include:
#   String (Default) - Accepts any text without slashes
#   Int              - Accepts positive integers
#   Path             - Similar to strings but also accepts slashes
#   UUID             - Accepts UUID strings (Search that up)

from flask import Flask
app = Flask(__name__) # Flask constructor -- Creates a flask app

# A decorator used to tell the application
# which URL is associated function
@app.route("/<name>")  # Defines a route
# Variables are used in the route by calling <varible_name> -- Makes a variable "name"
def hello_flask(name):  # Creates a function that is bound with "/" route and returns hello when the root page is accesssed
    return "Hello %s!" %name 

@app.route("/") # Defines another route
def home_flask(): # Function is bound to route
    return "Welcome to Home Page!" # Displays Message when the url is visited

@app.route("/<int:flaskID>") # This is the variable type Int. Accepts floats and signed ints too
def flask_id(flaskID):
    return "Flask ID - %d" %flaskID # Returns the flask ID

if __name__ == "__main__":
    app.run(debug=True) # Runs the app in debug mode -- Ensures the app does not need to restart manually if any changes are made in code
