from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return("hello world")

@app.route("/advay")
def answer():
    return("hello ADVAY")    

@app.route("/<string:name>")
def hello(name):
    return f"hello, {name}"
