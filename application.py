from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return("<h1>Hello World!!</h1>")
    print("<em>I hope everyone is having a wonderful day</em>")
    print("Today is quite nice")

@app.route("/<string:name>")
def hello(name):
    print(f"<h1>Hello, {name}!</em>")
    print(f"<em>I hope you are having a wonderful day, {name} </em>")
    print(f"<h2>The weather is quite nice today right, {name}</h2>")
