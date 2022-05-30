
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
	return "Hello world"


@app.route('/login')
def login():
	return "login"