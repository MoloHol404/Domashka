from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("./login.html")


@app.route("/login")
def hello():
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True)
