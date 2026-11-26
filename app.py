from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World! I'm using Flask."

@app.route("/higashi")
def higashi():
    return "東のページです！自治会の会計をLINEで楽にするサービスを作っています。"

@app.route("/Kimura")
def Kimura():
    return "Kimuraのページです！自治会をらくにするよ！！"

@app.route("/akiyama")
def akiyama():
    return "こんにちは＾＾"

@app.route("/Chu")
def Chu():
    return "yahho"

@app.route("/higashi_vscode")
def higashi_vscode():
    return "VSCodeから変更した"

@app.route("/kimura_vscode")
def kimura_vscode():
    return "俺がした"





@app.route("/hi^^")
def hi():
    return "hi~^^"

@app.route("/gaha")
def gaha():
    return "gahaha^^"