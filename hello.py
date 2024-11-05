from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/saludo")
def saludoatodos():
    return "<center> saludos a todos los que me lean</center>"

@app.route("/about")
def sobremi():
    return "<marquee><h1> aviel.pina@uabc.edu.mx <h1><marquee>"