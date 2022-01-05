from flask import Flask,render_template
import legkisebb
from leggyakoribb import leggyakoribbszamok
app = Flask(__name__)

@app.route("/index.html")
def index():
    return render_template("templates/index.html")

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/legkisebb.html")
def kicsi():
    kicsi = legkisebb.legkisebbszam()
    return render_template("legkisebb.html", kicsi=kicsi)

@app.route("/erdekes.html")
def erdekes():
    return render_template("erdekes.html")

@app.route("/grafikon.html")
def grafikon():
    return render_template("grafikon.html")

@app.route("/leghasonlobb.html")
def hasonlo():
    return render_template("leghasonlobb.html")

@app.route("/leghosszabb.html")
def hosszabb():
    return render_template("leghosszabb.html")

@app.route("/leggyakoribb.html")
def gyakoribb():
    return render_template("leggyakoribb.html")


if __name__ == "__main__":
    app.run(debug=True)

                