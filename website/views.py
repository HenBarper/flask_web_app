from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/hello')
def hello_world():
   return "<h1>hello world</h1>"

@views.route('/bye')
def bye_world():
   return "<h1>goodbye world</h1>"