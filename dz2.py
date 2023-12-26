from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
@app.route("/about")
def about():
    return render_template("bebre.html")


@app.route("/contacts")
def contacts():
    return render_template("contakti.html")


@app.route("/index")
def mainpage():
    return render_template("indexita.html")

if __name__ == "__main__":
    app.run(debug=True)
