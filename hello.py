from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

#def index():
#    return "<h1>Hello World!</h1>"


#FILTERS
#safe
#capitalize
#lower
#upper
#title
#trim
#striptrags

def index():
    first_name = "John"
    stuff = "This is <strong>Bold</strong> Text!"
    fav_pizza = ["Pepperoni", "Cheese", "Mushroom"]
    return render_template("index.html",
        first_name = first_name,
        stuff = stuff,
        fav_pizza = fav_pizza)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

#Create Custom Error Pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

