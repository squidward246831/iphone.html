from Flask import Flask
app = Flask(_name_)
@app.route("/")
def index():
    return("Hello World!!")
@app.route("/<string:name")
def hello(name):
    return("Hello, {name}!")    
