# Visit geeksforgeeks for flask tutorial

# Data types in Flask include:
#   String (Default) - Accepts any text without slashes
#   Int              - Accepts positive integers
#   Path             - Similar to strings but also accepts slashes
#   UUID             - Accepts UUID strings (Search that up)
#   Float            - Theres also floats apparently

from flask import Flask, redirect, url_for
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

@app.route("/<float:flaskID>") # This is the variable type Int. Accepts floats and signed ints too
def flask_id(flaskID):
    return "Flask ID - %f" %flaskID # Returns the flask ID

###### Example for dynamic binding for URLs
@app.route("/admin") # Decorator for root (argument) function
def hello_admin():  # Binding to hello_admin call
    return "Hello Admin"

@app.route("/guest/<guest>")
def hello_guest(guest): # Binding to hello_guest call
    return "Hello %s as Guest" %guest

@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":  # Dynamic binding for URL to function -- Dont forget to import redirect and url_for
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guest=name))

if __name__ == "__main__":
    app.run(debug=True) # Runs the app in debug mode -- Ensures the app does not need to restart manually if any changes are made in code
    print("Hello Flask")
