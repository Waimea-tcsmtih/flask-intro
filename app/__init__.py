from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from random import randint


# Create the app
app = Flask(__name__)
#--------------------------------------------------------------------------
# Home page - loading a static page
@app.get("/")
def home():
    return render_template('pages/home.jinja')
#--------------------------------------------------------------------------
# random - passing a random value into a template
@app .get("/random/")
def random():
    randNum = randint(1, 1000)
    return render_template('pages/random.jinja', number=randNum ) 
#--------------------------------------------------------------------------
# Number - getting a value from the root and passing it into the template
@app .get("/number/<int:num>")
def analyseNumber(num):
    print(f"You entered: {num}")
    return render_template('pages/number.jinja', number=num ) 
#--------------------------------------------------------------------------
# About page -  loading a static page
@app .get("/about/")
def about():
    return render_template('pages/about.jinja')
#--------------------------------------------------------------------------
# form page - static page with some forms
@app .get("/form")
def form():
    return render_template('pages/form.jinja')
#--------------------------------------------------------------------------
#Handle data posted form the form
@app.post("/processForm")
def processForm ():
    print(f"Form data: ${request.form}")
    return render_template(
        "pages/formData.jinja",
        name = request.form["name"],
        age = request.form["age"]
        )
#--------------------------------------------------------------------------
#handles any missing pages
@app.errorhandler(404)
def notFound(e):
    return render_template('pages/home.jinja')

