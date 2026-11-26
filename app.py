from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World! I'm using Flask."

@app.route("/higashi")
def higashi():
    return "東のページです！自治会の会計をLINEで楽にするサービスを作っています。"
