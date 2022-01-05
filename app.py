from flask import Flask,render_template
from legkisebb import legkisebbszam
from leggyakoribb import leggyakoribbszamok
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/legkisebb.html")
def kicsi():
    kicsi = legkisebbszam()
    return render_template("legkisebb.html",kicsi=kicsi)
            
if __name__ == "__main__":
    app.run(debug=True)

                