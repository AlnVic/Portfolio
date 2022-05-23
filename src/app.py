from flask import Flask, render_template, url_for
app = Flask(__name__)
@app.route("/")
def Portfolio():
    return render_template ("home.html")
@app.route("/Sobre")
def Sobre():
    return render_template ("sobre.html")
@app.route("/Serviços")
def Serviços():
    return render_template ("servicos.html")
@app.route("/Habilidades")
def Habilidades():
    return render_template ("habilidades.html")
@app.route("/Contatos")
def Contatos():
    return render_template ("contatos.html")
