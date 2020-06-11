from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return("<h1>Hello World!!</h1>")
    return("<em>I hope everyone is having a wonderful day</em>")
    return("Today is quite nice")

@app.route("/<string:name>")
def hello(name):
    return f"<h1>Hello, {name}!</em>"
    return f"<em>I hope you are having a wonderful day, {name} </em>"
    return f"<h2>The weather is quite nice today right, {name}</h2>"
    
