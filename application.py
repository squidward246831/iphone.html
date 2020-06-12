from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return("hello world")

@app.route("//")
def answer():
    return("Welcome Advay")

@app.route("/<string:name>")
def hello(name):
    return f"hello, {name}""
